import random
import sys

low = 1
high = 100

print("Guess a number between {0} and {1}".format(low, high))

guessnumb = 0
number = random.randint(low, high)

try:
	guess = int(input('What\'s your guess? '))
except ValueError:
	print("Couldn\'t convert input to Integer")
	continue

if guess < low or guess > high:
	print("Value out of range ({0} - {1})".format(low, high))
else:
	guessnumb += 1
	
	if guess < number:
		print("Your guess was too low")

	if guess > number:
		print("Your guess was too high")

	if guess == number:
		break
	
except KeyboardInterrupt:
	print("\n  ^C detected, terminating...")
	sys.exit()

except EOFError:
	print("\n  ^D detected, terminating...")
	sys.exit()

if guess == number:
	if guessnumb <5:
		print("Great, you guessed the number in {0} trys. You are good at this!".format(guessnumb))
	
	else:
		print("Lol, you guessed the number in {0} trys. You suck in this game".format(guessnumb))
