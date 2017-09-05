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

# List are mutable unlike strings
numbers[5] = 50 # replace the value at index 5 with 50
names[1] = 'Jefferson'
print(numbers)
print(names)

# Add values to the end of the list with append()
numbers.append(23 * 4)
names.append('Aristotle')
print(numbers)
print(names)

# Assign, change, and clear lists with slice
names[1:4] = ['Steven', 'Jaky', 'Alicia'] # Change values
print(names)
names[1:4] = [] # remove the changed values
print(names)
names[:] = [] # clear the list
print(names)

# Use len() to get lenght of list
print(len(names))
print(len(numbers))