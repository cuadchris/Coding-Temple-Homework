from math import pi

def squareFootage():
    length = int(input("Enter the length of your home in feet: "))
    width = int(input("Now the width: "))
    area = length * width
    print(f'Your home is {area} square feet!')

def circumference():
    radius = int(input("Enter the radius: "))
    circumference = 2 * pi * radius
    print(f'The circumference is {circumference}')
