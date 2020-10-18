'''
THE SPIDERWILL CRAWL THE WEB PAGE , STORE AND PROCESS THE WORDS
'''

import requests
from bs4 import BeautifulSoup
import operator

def crawler(url):
    word_list = []
    response = requests.get(url)
    plain_text = response.text
    soup = BeautifulSoup(plain_text , "html.parser")
    for tags in soup.findAll("div" , {"class" : "text show-more__control"}):
        sentence = tags.text
        words = sentence.lower().split()
        for word in words:
            word_list.append(word)
    clean_words(word_list)

def clean_words(word_list):
    clean_word_list = []
    symbols = "~!@#$%^&*()_+`=-{}|:\"<>?;'[]\,.'/1234567890"
    for word in word_list:
        for sym in symbols:
            word = word.replace(sym , "")
        if len(word) > 0:
            clean_word_list.append(word)
    create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    dict = {}
    for word in clean_word_list:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    for key , value in sorted(dict.items() , key = operator.itemgetter(1)):
       print(key , value)


crawler("https://www.imdb.com/title/tt7286456/reviews?ref_=tt_urv")
