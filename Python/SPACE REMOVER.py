Final = ''
text = input('TEXT HERE :\n')
for index, char in enumerate(text):
        if not(text[index] == " " and text[index+1]==" "):
            Final = Final + char
print(Final)
