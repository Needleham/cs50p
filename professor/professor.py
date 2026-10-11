'''
In a file called professor.py, implement a program that:

Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. 
No need to support operations other than addition (+).
Note: The order in which you generate x and y matters. 

Your program should generate random numbers in x, y pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).

Prompts the user to solve each of those problems. 
If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, 
allowing the user up to three tries in total for that problem. 
If the user has still not answered correctly after three tries, the program should output the correct answer.

The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, 
and generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

'''
#1 - Get user input for a level, needs a while loop to prompt again if not == 1 2 3
#2 - Generate a list containing an x and y value 
#3 - prompts user to solve + 
#4 - Check answer and tracks guess attempts
#5 - If guesses exceed 3 print answer and move one
#6 - Track correct and incorrect and once end print containing


import random



def main():
    level = get_level()
    score = 0 

    for i in range(10):
        num1 = generate_integer(level)
        num2 = generate_integer(level)
        solution = num1 + num2
        guesses = 0 

        while guesses < 3:
            try:
                guess = input(f"{num1} + {num2}= ").strip()
                guess = int(guess)
            except ValueError:
                print("EEE")
                guesses += 1 
                continue

            if guess == solution:
                score += 1
                break

            print("EEE")
            guesses += 1 

        if guesses == 3 and guess != solution:
            print(solution)

    print(f"Score: {score}")





def get_level():
    while True:
        try:
            level= input("Level: ").strip()
            if int(level) not in range(1, 4):
                raise ValueError
            else:
                return int(level)
        except ValueError:
            pass



def generate_integer(level):
    if level == 1:
        num = random.choice(range(0, 10))
    elif level == 2:
        num = random.choice(range(10, 100))
    elif level == 3:
        num = random.choice(range(100, 1000))
    return(num)
 

if __name__ == "__main__":
    main()
