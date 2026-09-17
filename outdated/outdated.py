"""
In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY),
otherwise known as middle-endian order, which is arguably bad design.
Dates in that format can’t be easily sorted because the date’s year comes last instead of first.
Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program
(e.g., a spreadsheet).
Dates in that format are also ambiguous. Harvard was founded on September 8, 1636,
but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates
should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country,
formatting years with four digits, months with two digits, and days with two digits,
“padding” each with leading zeroes as needed.

In a file called outdated.py, implement a program that prompts the user for a date, anno Domini,
in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the list below:
"""


def main():
    regDate = input("Date: ").strip()
    if "/" in regDate:
        bits = regDate.split(sep="/")
        if not bits[0].isdigit():
            continue
        date = regDate

    else:
        if "," not in regDate:
            continue

    print(convertDate)


def convertDate(date):

    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }

    while True:
        try:
            regDate = input("Date: ").strip()
            if "/" in regDate:
                bits = regDate.split(sep="/")
                if not bits[0].isdigit():
                    continue
                date = regDate
            else:
                if "," not in regDate:
                    continue
                date = regDate.replace(",", "").replace(" ", "/").title()

            month, day, year = date.split(sep="/")

            if month in months:
                month = months[month]

            if int(month) > 12 or int(day) > 31:
                continue

            convertedDate = "{year}-{int(month):02}-{int(day):02}"
            return convertedDate
            break

        except ValueError:
            pass


if __name__ == "__main__":
    main()
