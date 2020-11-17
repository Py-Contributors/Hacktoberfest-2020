import getpass

# Enter a word, her input will be hidden
hangman = getpass.getpass('Type a word: ')

# You will have a maximum of 3 attempts
print('Your goal is to get the word typed right. You can make a maximum of 3 mistakes')
print('\n')

letters = []
mistakes = 3

while True:
    if mistakes == 0:
        print('\033[31m\nYOU LOST!!!\033[0m')
        break

    # Enter a letter
    letter = input('Type a letter: ')

    if len(letter) > 1:
        print("\nPlease enter only one letter\n")
        continue

    if letter in hangman:
        print(f'The letter "{letter}" exists in the word')
        letters.append(letter)
    else:
        print(f'A letter "{letter}" does not exist in the word')
        mistakes -= 1
        print(f'You have {mistakes} mistakes')

    hangman_temp = ''
    for letter_secret in hangman:
        if letter_secret in letters:
            hangman_temp += letter_secret
        else:
            hangman_temp += '*'

    if hangman_temp == hangman:
        print(
            f'\033[32m\nYOU HIT the word! The word was: {hangman}\033[0m')
        break
    else:
        if mistakes != 0:
            print(
                f'\033[34m\nThe word looks like this: {hangman_temp}\n\033[0m')
