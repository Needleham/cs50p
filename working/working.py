'''
In a file called working.py, implement a function called convert that expects a str in any of the 12-hour formats
below and returns the corresponding str in 24-hour format (i.e., 9:00 to 17:00).
Expect that AM and PM will be capitalized (with no periods therein) and that there will be a space before each.
Assume that these times are representative of actual times, not necessarily 9:00 AM and 5:00 PM specifically.

9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM
Raise a ValueError instead if the input to convert is not in either of those formats or if either time is invalid
(e.g., 12:60 AM, 13:00 PM, etc.). But do not assume that someone’s hours will start ante meridiem and end post meridiem;
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).

Structure working.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit,
but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.
'''

import re
import sys

def main():
    s = input("Hours: ")
    a = convert(s)
    print(a)

def convert(s):
    a = re.search("([0-9]{1,2})(?::([0-9]{2}))? (AM|PM) to ([0-9]{1,2})(?::([0-9]{2}))? (AM|PM)", s)

    if a == None:
        raise ValueError

    hour = int(a.group(1))
    minutes = a.group(2)
    if minutes is None:
        minutes = "00"
    x = a.group(3)

    hour2 = int(a.group(4))
    minutes2 = a.group(5)
    if minutes2 is None:
        minutes2 = "00"
    y = a.group(6)

    if hour > 24:
        raise ValueError
    if hour2 > 24:
        raise ValueError


    if hour == 12 and x == "AM":
        hour = str("0")
    elif hour == 12 and x == "PM":
        hour = 12
    elif x == "PM":
        hour = (hour + 12)
    if int(hour) < 10:
        hour = str(f"0{hour}")
    else:
        hour = str(hour)


    if hour2 == 12 and y == "AM":
        hour2 = str("0")
    elif hour2 == 12 and y == "PM":
        hour2 = 12
    elif y == "PM":
        hour2 = (hour2 + 12)
    if int(hour2) < 10:
        hour2 = str(f"0{hour2}")
    else:
        hour2 = str(hour2)


    if int(minutes) >= 60:
        raise ValueError
    if int(minutes2) >= 60:
        raise ValueError

    return f"{hour}:{minutes} to {hour2}:{minutes2}"

if __name__ == "__main__":
    main()
