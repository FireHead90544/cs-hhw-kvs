# Program to check if year is a leap year or not
# Programmed by Rudransh Joshi
# Class: XI - A (Second Shift)

import os # Just to clear the garbage data in from the terminal
os.system("cls") # Just to clear the garbage data in from the terminal


def is_leapyear(year):
    if (year % 4) == 0:  # Checking for conditions for leap year viz. 4, 100, 400 and printing the output
        if (year % 100) == 0:
            if (year % 400) == 0:
                print(f"{year} is a leap year.\n")
            else:
                print(f"{year} is not a leap year.\n")
        else:
            print(f"{year} is a leap year.\n")
    else:
        print(f"{year} is not a leap year.\n")


while True:
    year = int(input("Enter a year: \t"))   # Taking Input
    is_leapyear(year)  # Running the function