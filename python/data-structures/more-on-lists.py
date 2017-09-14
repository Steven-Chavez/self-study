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

# using del list[:] to remove all items from list
del name[:]
print(name)

# index(x[,start[,end]])
farm = ['chicken', 'cow', 'pig', 'goat']
index = farm.index('cow')
print(farm[index])

# count(x) method returns the number of times item appears
farm.append('chicken') # add item to list
print(farm.count('chicken'))

# sort(key=None, reverse=False) method sorts list
# see sorted() to customize sort() arguments
farm.sort()
print(farm)

# reverse() method reverses items in list
farm.reverse()
print(farm)

# create a copy of a list
copy = farm[:]
print(copy)

# Use a list as a stack
''' Using a list as a Stack a stack is where the last
element is added is the first element recieved'''
stack = [1, 2, 3, 4]
stack.append(5) # Add item to the end of the list
stack.append(6) # Add item to the end of the list
print(stack)

print('Pop last element added: ' + str(stack.pop()))
print(stack)

# Using a List as a Queue
'''A Queue is first-in first-out. A list is naturally slow at
acting as a queue. Poping from the beginning is slow because
the all of the items have to be shifted by one. This is solved
by using collections.deque'''
from collections import deque
queue = deque(['A', 'B', 'C'])
queue.append('D')   # add item to the end of list
queue.append('E')   # add another item to the end of the list
print(queue)        # display updated list
queue.popleft()     # pop 'A' from list
queue.popleft()     # pop 'B' from list
print(queue)        # display updated list
