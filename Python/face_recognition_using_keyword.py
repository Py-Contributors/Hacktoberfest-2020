import zipfile
import io
import copy

from PIL import Image
from PIL import ImageDraw
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# Create handle to zipfile
ziphandle = zipfile.ZipFile(input("Enter zipfile name: "))
filenames = ziphandle.namelist()

keyword = input("Enter keyword: ")
size = (128, 128)
# Create header
size_header = (50, 25)
header = Image.new('RGB', size_header, (255, 255, 255))

sheets = []

for filename in filenames:
    # Extract file from zip in memory
    get_img = ziphandle.read(filename)
    
    # Then as a flie type handle
    fh = io.BytesIO(get_img)
    img = Image.open(fh)
    
    # Checking if the keyword is in the image's text
    text = pytesseract.image_to_string(img)
    if keyword in text:
        # Detecting faces
        copy_image = img.copy()
        open_cv_version = copy_image.convert("L")
        open_cv_version.save("grey.png")
        cv_img = cv.imread("grey.png")
        faces = face_cascade.detectMultiScale(cv_img, 1.35)
        drawing = ImageDraw.Draw(copy_image)
        for x, y, w, h in faces:
            drawing.rectangle((x, y, x + w, y + h), outline = "red")
        if faces.size != 0:
            # Extracting faces
            faces_images = []
            for face in faces:
                face_image = img.crop((face[0], face[1], face[2] + face[0], face[3] + face[1]))
                face_image.thumbnail(size)
                faces_images.append(face_image)
            # Creating faces contact sheet
            first_face = faces_images[0]
            faces_contact_sheet = Image.new(first_face.mode, (first_face.width * 5, 
                                                              first_face.height * (int(len(faces_images) / 5) + 1)))
            x = 0
            y = 0
            
            for face in faces_images:
                faces_contact_sheet.paste(face, (x, y))
                if x + first_face.width == faces_contact_sheet.width:
                    x = 0
                    y += first_face.height
                else:
                    x += first_face.width
            faces_contact_sheet = faces_contact_sheet.resize((int(faces_contact_sheet.width / 2),
                                                              int(faces_contact_sheet.height / 2)))
            
            header = header.resize((faces_contact_sheet.width, 25))
            
            sheets.append(faces_contact_sheet)
        else:
            no_faces_found = Image.new('RGB', (header.width, header.height), (255, 255, 255))
            ImageDraw.Draw(no_faces_found).text((0, 0), "But there were no faces in that file!", (0, 0, 0))
            sheets.append(no_faces_found)
            
# Find the final image size
width = sheets[0].width
height = 0
for sheet in sheets:
    height += sheet.height + header.height

# Create the final image
x = 0
y = 0
final_contact_sheet = Image.new('RGB', (width, height))
for i in range(len(sheets)):
    s = "Results found in file " + filenames[i]
    copy_header = header.copy()
    ImageDraw.Draw(copy_header).text((0, 0), s, (0, 0, 0))
    final_contact_sheet.paste(copy_header, (x, y))
    y += copy_header.height
    final_contact_sheet.paste(sheets[i], (x, y))
    y += sheets[i].height

display(final_contact_sheet)