#!/usr/bin/env python3

"""
Author: Nathaniel Weeks
Date:   8/21/2018
Class:  BUSA 342 Practical Programming: Python
Description:
    This program takes two user inputs and combines them as a string. It 
    then does this again but converts the user input to numbers and finds the
    sum. 
"""

# Get two names from the user and store them in variables
first_name = input('Please enter the first name: ')
second_name = input('Please enter the second name: ')
# Print the concatenated user names
print(first_name + second_name)

# Get two numbers from the user and store them in variables
first_number = input('Please enter the first number: ')
second_number = input('Please enter the second number: ')
# Convert the strings to numbers (whole numbers in this case)
first_number = int(first_number)
second_number = int(second_number)
# Print the sum of the two numbers entered
print(first_number + second_number)
