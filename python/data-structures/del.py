# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/16/17
# File: del.py

# del statement
'''Unlike the pop() method the del statement does not return
a value. It simply deletes the item at the given index or
slice expression'''

# initialize list for testing using list comprehension
test = [x**2 for x in range(1,11)]
print(test)

# use del statement to delete item at a specific index
del test[3]
print(test)

# use a slice expression to delete a section of the list
del test[4:7]
print(test)

# empty entire list using del statement
del test[:]
print(test)

