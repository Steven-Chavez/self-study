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

# Use extend() method
name[len(name):] = name
print(name)

name[len(name):] = ['Georgia', 'Helen']
print(name)
