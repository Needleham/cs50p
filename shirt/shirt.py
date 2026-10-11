'''
In a file called shirt.py, implement a program that expects exactly two command-line arguments:

in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output
The program should then overlay shirt.png (which has a transparent background) on the input after resizing and 
cropping the input to be the same size, saving the result as its output.

Open the input with Image.open, resize and crop with Image.Ops.fit using default values for 
method, bleed and centering. Overlay the shirt with Image.paste and save the result with Image.save

'''

import sys
from PIL import Image, ImageOps



def main():
    images = getInput()
    image1 = images[0]
    shirt = Image.open("shirt.png")
    output = images[1]
    createImage(image1, shirt, output)

    


def getInput():
    suffixes = (".jpg", ".jpeg", ".png")
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many arguments")
    elif not sys.argv[1].endswith(suffixes) or not sys.argv[2].endswith(suffixes):
        sys.exit("Incorrect file type")

    image1suffix = sys.argv[1].split(".")
    outputsuffix = sys.argv[2].split(".")
    if image1suffix[1] != outputsuffix[1]:
        sys.exit("Mismatched File types")
    file1 = sys.argv[1]
    file2 = sys.argv[2]
    return file1, file2 


def createImage(image1, shirt, output):
    try:
        im1 = Image.open(image1)
    except FileNotFoundError:
        sys.exit("Missing file")
    im1 = ImageOps.fit(im1, shirt.size)
    im1.paste(shirt, mask=shirt)
    im1.save(output)


if __name__ == "__main__":
    main()
