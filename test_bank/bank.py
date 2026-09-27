'''
In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y,
wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage rounded to the
nearest integer, how much fuel is in the tank.

If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

'''

def main():
    fraction = input("Fractions: ").strip()
    n, d= convert(fraction)
    percent = gauge(n, d)
    print(percent)


def convert(fraction):
    try:
        nom, delim = fraction.split("/")
        n = int(nom)
        d = int(delim)
        return n, d
    except(ValueError, ZeroDivisionError):
        pass

def gauge(n, d):
    if n >= 0 and d >= 1 and n <= d:
        p = round(int(n) / int(d) * 100)
        percent = int(p)
        if percent >= 99:
            return("F")
        elif percent <= 1:
            return("E")
        else:
            return(percent)

if __name__ == "__main__":
    main()
