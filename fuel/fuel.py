"""
In a file called fuel.py, implement a program that prompts the user for a fraction,
formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer,
and then outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank.

If, though, 1% or less remains, output E instead to indicate that the tank is essentially
empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt
the user again.
(It is not necessary for Y to be 4.)

Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""

while True:
    user = input("Fractions: ").strip()
    try:
        nom, delim = user.split("/")
        n = int(nom)
        d = int(delim)

        if n >= 0 and d >= 1 or n > d:
            p = round(int(nom) / int(delim) * 100)
            percent = int(p)
            if percent >= 99:
                print("F")
            elif percent == 1:
                print("E")
            elif percent == 0:
                print("E")
            else:
                print(f"{percent}%")
            break
    except (ValueError, ZeroDivisionError):
        pass
