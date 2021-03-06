# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/17/17
# File: tuple.py
# Resource: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

# Tuples and Sequences.
'''A tuple is an immutable container that is made up of a number
of values separated by commas''' 

# Populate tuple with values for testing.
test = 2039, 'hello', 8493, 'world'

# Access tuple data and print.
print(test[1] + ' ' + test[3])
print(test)

# Nesting tuples
nest = test, ('a', 'b', 'c', 'd')
print(nest)

# Tuples are immutable. The below statement produces an error
# test[2] = 1111

# Initialize empty and single item tupple
empty = () 
single = 283,   # needs a trailing comma
print(empty)
print(single)

# Sequence unpacking of a tuple
a , b, c, d = test
print(test) 
print(a)
print(b)
print(c)
print(d)
