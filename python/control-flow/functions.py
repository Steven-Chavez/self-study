# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/7/2017
# File: functions.py
# Resource: https://docs.python.org/3/tutorial/controlflow.html

# Basic function defining
def addition(n, m):
	'''Adds both arguments together'''
	sum = n + m
	return sum

total = addition(20, 80) # Call function
print(total)
print(addition.__doc__) # Displays functions docstring

# Defualt argument values allow you to set default values
def subtraction(n = 9, m = 6):
    '''Subtract both arguments'''
    sum = n - m
    return sum

total = subtraction()
print(total)

