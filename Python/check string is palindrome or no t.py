phrase = str(input("Digite a frase que será invertida: ")).strip().upper() #Receive the phrase
words = phrase.split() # spliting the word
together = "".join(words) # joining the words
inverse = "" #inverting a word
for letter in range(len(junto)-1, -1, -1): #creating the loop
    inverse += together[letra]
print(together, inverse) #showind the words
if inverse == together: #Checking
    print("Yes, is a  palindrome") #result
else:
    print("Sorry, isn't a palindrome")#result
