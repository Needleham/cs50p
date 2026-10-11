'''
In a file called numb3rs.py, implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, 
respectively, if that input is a valid IPv4 address or not.

Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, 
but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.
'''


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        numbers = ip.split(".")
        if len(numbers) != 4:
            return False

        a = int(numbers[0])
        b = int(numbers[1])
        c = int(numbers [2])
        d = int(numbers [3])

        if a > 255 or b > 255 or c > 255 or d > 255:
            return False
        elif a < 0 or b < 0 or c < 0 or d < 0:
            return False
        return True




    except (IndexError, ValueError):
        return False



if __name__ == "__main__":
    main()


