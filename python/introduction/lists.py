# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/4/2017
# File: strings.py
# Resource: https://docs.python.org/3/tutorial/introduction.html

# Lists are used to group togther values.

# Basic list format
numbers = [2, 5, 10, 33]
names = ['Tesla', 'Edison', 'Nikola']

# Indexing and slicing lists
print(numbers[3])					#indexing
print(names[2] + ' ' + names[0])	#indexing
print(numbers[:2])					#slicing returns new list
print(names[-1:])					#slicing 

# Concatenating lists
numbers = numbers + [44, 22, 56]
names = names + ['Thomas', 'Socrates']
print(numbers)
print(names)

