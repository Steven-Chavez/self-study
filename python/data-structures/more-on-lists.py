# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/11/2017
# File: more-on-lists.py
# Resource:https://docs.python.org/3/tutorial/datastructures.htm

# This document will cover all of the methods for lists
name = ['Tesla', 'Steven', 'Jaky', 'Breanna', 'Alicia']

# Use append(x) to add an item to the end of list
name.append('Pedro')
print(name)

# Use extend(iterable) method. like apend but more than one item
name.extend(name)
print(name)

name.extend(['Georgia', 'Helen'])
print(name)

# insert(i,x) method inserts an item at specific position
name.insert(0, 'Rose')
print(name)

# remove(x) method deletes item 
name.remove('Rose')
print(name)

# pop([i]) returns and removes item at given position
# If used without arguments pop() removes and returns last item
pop = name.pop()
print(pop)

pop = name.pop(0)
print(pop)
