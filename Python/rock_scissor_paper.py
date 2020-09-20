import random

compScore = 0
playerScore = 0


def ShowScore():
    print("-" * 80)
    print(
        f"################    Computer Score  : {compScore}     ################"
    )
    print(
        f"################       PlayerScore  : {playerScore}     ################"
    )
    print("-" * 80, "\n\n")


def welcome():
    print("Welcome to Rock[0] Paper[--] Scissors[8<]")
    print("Your Turn")
    print("choose:\n R for ROCK    [0]\n P for PAPER   [--]\n S for SCISSOR [8<]\n")
    print("Press Q for Exit")


welcome()

playAgain = True
while playAgain:

    u = input().lower()
    a = ["Rock", "Paper", "Scissors"]
    c = random.choice(a)

    if u == "q":
        playAgain = False

    elif compScore > 2:
        print(
            f"Computer Win The Series By {compScore} - {playerScore} \nP : Play  Q : Exit\n"
        )
        if u == "p":
            compScore = 0
            playerScore = 0
            welcome()

    elif playerScore > 2:
        print(
            f"You Win The Series By {playerScore} - {compScore}\nP : Play  Q : Exit\n"
        )
        if u == "p":
            compScore = 0
            playerScore = 0
            welcome()

    elif u == "r":
        if c == "Rock":
            print(f" You both chosen {c} \n Its a DRAW")
        elif c == "Paper":
            print(f"You : ROCK \nComputer : {c} \nYou Lose")
            compScore += 1
        elif c == "Scissors":
            print(f"You : ROCK \nComputer : {c} \nYou Win")
            playerScore += 1
        ShowScore()

    elif u == "p":
        if c == "Paper":
            print(f" You both chosen {c} \n Its a DRAW")
        elif c == "Rock":
            print(f"You : PAPER \nComputer : {c} \nYou Win")
            playerScore += 1
        elif c == "Scissors":
            print(f"You : PAPER \nComputer : {c} \nYou Lose")
            compScore += 1
        ShowScore()

    elif u == "s":
        if c == "Scissors":
            print(f" You both chosen {c} \n Its a DRAW")
        elif c == "Paper":
            print(f" You : SCISSOR \nComputer : {c} \nYou Win")
            playerScore += 1
        elif c == "Rock":
            print(f"You : SCISSOR \nComputer : {c} \nYou Lose")
            compScore += 1
        ShowScore()
    else:
        print("Please chose the right option this time")