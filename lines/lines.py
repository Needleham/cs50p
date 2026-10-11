'''
Even so, in a file called lines.py, implement a program that expects exactly one command-line argument, 
the name (or path) of a Python file, and outputs the number of lines of code in that file, 
excluding comments and blank lines. 
If the user does not specify exactly one command-line argument, 
or if the specified file’s name does not end in .py, 
or if the specified file does not exist, 
the program should instead exit via sys.exit.

Assume that any line that starts with #, optionally preceded by whitespace, is a comment. 
(A docstring should not be considered a comment.) Assume that any line that only contains whitespace is blank.

'''
import sys

def main():
# Get user input to open a file and check for file not found Error
# Check for command line argument
    file = fileCheck()
    message = lineCount(file)
    print(message)

def fileCheck():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")
    else:
        f = sys.argv[1]

    return f

def lineCount(file):
    try:
        count = 0 
        with open(file, "r") as f:
            for line in f:
                if line.strip() and not line.lstrip().startswith("#"):
                    count += 1
                else:
                    continue
            return count
    except FileNotFoundError:
        sys.exit("File does not exist")



if __name__ == "__main__":
    main()

