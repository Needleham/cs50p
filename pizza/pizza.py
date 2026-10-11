'''
In a file called pizza.py, implement a program that expects exactly one command-line argument,
the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, 
a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. 

If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, 
or if the specified file does not exist, the program should instead exit via sys.exit.
'''

from tabulate import tabulate
import sys
import csv

def main ():
    file = get_csv()
    message = format(file)
    print(message)


def get_csv():
    if len(sys.argv) < 2:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Incorrect file type")
    else:
        c = sys.argv[1]

    return c

def format(file):
    try:
        with open(file, newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            return(tabulate(reader, headers={1: "Scilian Pizza", 2: "small", 3: "large"}, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()

