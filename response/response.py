'''
When creating a Google Form that prompts users for a short answer (or paragraph), it’s possible to enable response validation
and require that the user’s input match a regular expression. For instance, 
you could require that a user input an email address with a regex like this one:

Or you could more easily use Google’s built-in support for validating an email address, 
per the screenshot below, much like you could use a library in your own code:

In a file called response.py, using either validator-collection or validators from PyPI, implement a program that 
prompts the user for an email address via input and then prints Valid or Invalid, respectively, 
if the input is a syntatically valid email address. 
You may not use re. And do not validate whether the email address’s domain name actually exists.
'''

from validator_collection import validators, checkers, errors 

def main():
    email = input("What's your email address? ").strip()
    e = email_check(email)

    print(e)

def email_check(email):
    try:
        e = checkers.is_email(email)
        if e == True:
            return "Valid"
        else:
            return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"
    except errors.EmptyValueError:
        return "Invalid" 

if __name__ == "__main__":
    main()


