# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/4/2017
# File: for.py
# Resource: https://docs.python.org/3/tutorial/controlflow.html

# The Python for statement is not the same as a for loop
# The for statement reminds of the PHP and C# foreach statement

# Create a list to iterate through
animals = ['chicken', 'goats', 'ducks', 'pigs']

# Basic for statement examples
for a in animals:
	print(a)

# Making a copy is recommended when you want to modify the list 
# your iterating through
for a in animals[:]:
	if len(a) == 5:
		animals.insert(0, a)
print(animals)