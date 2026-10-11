'''
In a file called scourgify.py, implement a program that:

Expects the user to provide two command-line arguments:
- the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, 
- and the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

Converts that input to that output, splitting each name into a first name and last name. 
Assume that each student will have both a first name and last name.
If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.
'''
import sys
import csv

def main():
    files = getFiles()
    file1 = files[0]
    file2 = files[1]
    final = conversion(file1, file2)
    print(final)

def getFiles():
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Incorrect file type")

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    return file1, file2 


def conversion(file1, file2):
    try:
        with open(file1, newline="") as csv1:
            reader = csv.DictReader(csv1)
            with open(file2, "w", newline="") as csv2:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(csv2, fieldnames=fieldnames)
                for row in reader:
                    #Need to split name 
                    name = row
                    first, last = name.split(" ")
                    writer.writerow(file2)
        return file2
    except FileNotFoundError:
        sys.exit("File not found")




if __name__ == "__main__":
    main()
