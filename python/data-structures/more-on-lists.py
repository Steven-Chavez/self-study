# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/11/2017
# File: more-on-lists.py
# Resource:https://docs.python.org/3/tutorial/datastructures.htm

# This document will cover all of the methods for lists
name = ['Tesla', 'Steven', 'Jaky', 'Breanna', 'Alicia']

# Add an item to the end of list
name.append('Pedro')
print(name)

# Use extend() method. like apend but more than one item
name.extend(name)
print(name)

name.extend(['Georgia', 'Helen'])
print(name)

# insert() method inserts an item at specific position
name.insert(0, 'Rose')
print(name)
