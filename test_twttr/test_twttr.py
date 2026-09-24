'''
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects 
a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.same


import re


twitter = input("Input: ")

twttr = re.sub(r'[a,e,i,o,u,A,E,I,O,U]','', twitter)

print(twttr)
'''
import re


def main():

    word = input("Input: ")
    shortened = shorten(word)
    print(shortened)


def shorten(word):
    word = re.sub(r'[aeiouAEIOU]', '', word)
    return word


if __name__ == "__main__":
    main()


