#!/usr/bin/env python
# coding: utf-8

### FOR SCRAPING QUESTION AND ANSWER PAIRS / FAQS ###


import requests
from selenium import webdriver

driver = webdriver.Chrome(r'C:\Users\Downloads\chromedriver_win32\chromedriver')



### Insert URL here ###

driver.get("")





from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html5lib')
#soup
soup_s = str(soup)
ls = soup_s.split()

### In case answers and questions are in the form of text and not in separate tags ###

answers = []
for header in soup.find_all('TAG_NAME'):
    out = []
    question = header.text.strip()
    next_tag = header
    i = 0
    
    while True:
        next_tag = next_tag.next_sibling
        if next_tag is None or next_tag.name == 'TAG_NAME':
            break
        if next_tag.name is not None:
            out.append(next_tag.text.strip())
    answers.append((question, out))
    
answers


### For removing unwanted promotional material / other links which are repeated ###

for span in soup.find_all("TAG_NAME", {'class':'ATTRIBUTE_NAME'}): 
    span.decompose()

### Questions ###

b = soup.find_all('TAG_NAME', attrs={'class':'ATTRIBUTE_NAME'})
b





### Answers ###
### I HAVE FILLED EXAMPLES OF TAG AND ATTRIBUTE NAMES HERE ###


results = soup.find_all('div', attrs={'class':'accordion-item-content'})
results





### For separable questions and answers example - collapsible panels etc. ###

answers = []
i = 0

for result in results:
    question = b[i].text.strip()
    out = result.text[0:-1].strip()
    urls = []
    if(result.find('a')):
        for link in result.find_all('a'):
            try:
                url = link['href']
                if url.startswith('/'):
                    	### Add site name here so that url scraped can be used directly later ###

			url = "" + url
            
                urls.append(url)
                
            except KeyError:
                pass

    else: 
        url = None
        urls.append(url)
    
    answers.append((question, out, urls))
    
answers


### Convert and view data as Data Frame ###


import pandas as pd
df1 = pd.DataFrame(answers, columns=['question','answer', 'url'])
#df1.drop_duplicates(subset = "question", keep = 'first', inplace = True)
df1



### Add scraped data to csv file ###

df1.to_csv('FILE_NAME',mode = 'a', index=False, encoding='utf-8')
pd.read_csv('FILE_NAME', encoding = 'utf-8')



### Convert Jupyter Notebook to python script ###

get_ipython().system('jupyter nbconvert --to script Web_Scraping.ipynb')