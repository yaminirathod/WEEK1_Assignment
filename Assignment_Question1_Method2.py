# 1. Write a Python program which accepts the radius of a circle from the user and compute the area.
# Developed by : Yamini Rathod C0796390
# Date : 16-05-2021

# Method 2 : Using simple Python Statements with Modules

# The Area of Circle = 3.14 * Radius * Radius

def calculateArea():
    radius = float(input('Please enter the Radius of a Circle : '))
    area = 3.14 * radius * radius
    print('The Area of a Circle is {:.2f}'.format(area))

def main():
    print('The program to find Area from the Radius of a Circle. Prepared by : Yamini Rathod C0796390')
    calculateArea()
main()