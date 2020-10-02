from random import randint
import random
import time

def game():
        player = input('Rock(r), Paper(p), Scissors(s) : ')

        choosen = randint(1,3)

        if choosen == 1:
                computer = 'r'
        elif choosen == 2:
                computer = 'p'
        else:
                computer = 's'

        print(player + ' vs ' + computer)

        print(computer)

        if player == computer:
                print('DRAW')
        elif player == 'r' and computer == 's':
                print('Player Wins!!')
        elif player == 'r' and computer == 'p':
                print('Computer Wins!!')
        elif player == 'p' and computer == 's':
                print('Computer Wins!!')
        elif player == 'p' and computer == 'r':
                print('Player Wins!!')
        elif player == 's' and computer == 'p':
                print('Player Wins!!')
        elif player == 's' and computer == 'r':
                print('Computer Wins!!')

##        time.sleep(2)

def playAgain():
        print('Do you want to play again?')
        return input().lower().startswith('y')

while True:
        game()
        if not playAgain():
                break
