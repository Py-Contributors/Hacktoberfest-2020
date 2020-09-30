#Auto Correcting the given word.

#Use "pip install textblob" to install the package textblob.

#imports the textblob library
from textblob import TextBlob

#We can put the word or sentence in variable or take it as an input.
#E.g: word = "Pogrram"
word = input("Enter the String: ")

correctWord = TextBlob(word)
print("The correct String is: ", correctWord.correct())