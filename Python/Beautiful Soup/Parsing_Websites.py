import urllib.request
import urllib.parse
import re 

url = 'https://pythonprogramming.net/beginner-python-programming-tutorials/'
values = {'s': 'basics',
        'submit' :'search'}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url,data)
resp = urllib.request.urlopen(req)
respData = resp.read()

#The code above will take all the metadata from the website a
#use regular expression 

#print(respData)
#produce lot of Junk stuff of the URL Stuff 
#Only want the paragraph data 
#The content you want is mainy the <p> tag 

paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
#. -> any character * -> 0 or more repeat ? -> one or more repeats

for eachP in paragraphs:
    print(eachP)

#This code will take all the stuff within the paragraph section and present what there