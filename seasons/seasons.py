'''
In a file called seasons.py, implement a program that prompts the user for their date of birth in YYYY-MM-DD format 
and then sings prints how old they are in minutes, rounded to the nearest integer, using English words instead of numerals, 
just like the song from Rent, without any and between words. 
Since a user might not know the time at which they were born, assume, for simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. 
and assume that the current time is also midnight. 
In other words, even if the user runs the program at noon, assume that it’s actually midnight, on the same date. 
Use datetime.date.today to get today’s date, per docs.python.org/3/library/datetime.html#datetime.date.today.
'''

import datetime
import inflect
import sys


def main():
    dob = input("Date of Birth: ").strip()
    time = conversion(dob)
    
    print(time)

def conversion(dob):
    try:
        c = datetime.date.today()

        year, month, day = dob.split("-")
        year = int(year)
        month = int(month)
        day = int(day)

        p = datetime.date(year=year, month=month, day=day)
        diff = c - p
        minutes = round(diff.total_seconds() / 60)


        # Convert to words
        w = inflect.engine()

        words = w.number_to_words(minutes, andword='').capitalize()

        return (f"{words} minutes")

    except ValueError:
        sys.exit("Invalid Date")

if __name__ == "__main__":
    main()


