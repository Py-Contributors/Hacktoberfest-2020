#make sure you instll pip install pyshortners 
from pyshortners import *
url = Shortener()
main_url = url.tinyurl.short("Required Url")
print(main_url)