# Write your code here
import random

words = ['python', 'java', 'kotlin', 'javascript', 'github', 'hacktoberfest', 'opensource']

letters = []

tries = 8

secret_word = random.choice(words)

def hide_word():
    new_string = ""
    global tries

    for x in secret_word:
        if x in letters:
            new_string = new_string + x
        else:
            new_string = new_string + '-'

    return new_string

print("H A N G M A N")
if input("Type 'play' to play the game, 'exit' to quit:") == "exit":
    exit()


print()
print(hide_word())

while True:
    letter = input("Input a letter: ")

    if len(letter) != 1:
        print("You should input a single letter\n")

        print(hide_word())
        continue

    if letter.isalpha() == False or letter.isupper():
        print("It is not an ASCII lowercase letter\n")

        print(hide_word())
        continue


    if letter in letters:
        print("You already typed this letter")
    elif letter not in secret_word:
        print("No such letter in the word")
        tries = tries - 1




    letters.append(letter)

    if tries == 0:
        print("You are hanged!")
        break

    print("")

    good_word = hide_word()

    print(good_word)


    if good_word == secret_word:
        print("You guessed the word!")
        print("You survived!")
        break
