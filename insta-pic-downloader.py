from selenium import webdriver
import urllib.request

driver= webdriver.Chrome(executable_path='D:\\Softwares\\chromedriver.exe')
profile_name= input('Enter the insta profile >')

#it will open the insta profile
driver.get('https://www.instagram.com/'+ profile_name)
driver.find

#bio= driver.find_element_by_xpath('//div[@class="-vDIg"]')
#text= bio.get_attribute('textcontent')

#print(text)

#it finds the image attribute 
image= driver.find_element_by_xpath('//img[@class="_6q-tv"]')
image_link= image.get_attribute('src') # it will extract the link

path= "D\\Hacking Scripts\\pics" + profile_name + '.jpg'  # it save the pic in this path
urllib.request.urlretrieve(image_link, path)  # it will extract the image from the link

print('pic downloaded')
