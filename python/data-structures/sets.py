# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/19/2017
# File: sets.py
# Resource: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

# Sets
'''A set is an unordered collection with no duplicate item'''

# Create sets using curly braces or the set() function
letters = {'a', 'z', 'i', 'a', 'b', 'b', 'z', 'w'}
print(letters)

# Create set using set() function
letters = set('aziabbzw')
print(letters)

# Check if items are in sets
boolean = 'a' in letters
print(boolean)
boolean = 'm' in letters
print(boolean)

# Test operation on two different words
one = set('amanda')
two = set('abraham')
print(one)
print(two)
print(one - two)
print(one | two)
print(one & two)
print(one ^ two)
