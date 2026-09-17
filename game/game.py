"""
In a file called game.py, implement a program that:

Prompts the user for a level, 𝑛.
If the user does not input a positive integer, the program should prompt again.

Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
Prompts the user to guess that integer.

If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small!
and prompt the user again.
If the guess is larger than that integer, the program should output Too large!
and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
"""

import random

while True:
    try:
        numRange = input("Level: ").strip()
        numRange = int(numRange)
        if numRange <= 0:
            continue
        elif numRange > 0:
            break
    except ValueError:
        print("Invalid Input")

num = random.randrange(1, stop=numRange + 1)


while True:
    try:
        guess = input("Guess: ").strip()
        guess = int(guess)
        if guess <= 0:
            continue
        if guess == num:
            print("Just right!")
            break
        elif guess > num:
            print("Too large!")
        elif guess < num:
            print("Too small!")

    except ValueError:
        pass
