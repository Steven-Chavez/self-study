# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/4/2017
# File: if.py
# Resource: https://docs.python.org/3/tutorial/controlflow.html

# if statements are the most well know statements
number = int(input("Please enter a number between 1-10 "))

# elif is short for else if 
if number <= 0:
	print('Not in range: Less than 1')
elif number > 10:
	print('Not in range: More than 10')
else:
	print('In range: ' + str(number))