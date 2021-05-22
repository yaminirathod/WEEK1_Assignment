# 2. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
# Developed by : Yamini Rathod C0796390
# Date : 16-05-2021

# Method 2 : Using simple Python Statements with Modules

def rev():
    fname = input('Please enter the first name : ')
    lname = input('Please enter the last name : ')
    print("Output")
    print(lname + " " + fname)

def main():
    print('The program to reverse the first name and last name with a space. Prepared by : Yamini Rathod C0796390')
    rev()
main()