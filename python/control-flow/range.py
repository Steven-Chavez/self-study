# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/4/2017
# File: range.py
# Resource: https://docs.python.org/3/tutorial/controlflow.html

# The range() function allows you iterate through numbers

# Combining a for statement and the range() function acts
# more like a traditional for loop
for i in range(10):
	print(i)
	
# You are able to set starting number
for i in range(5, 11):
	print(i)
	
# You are able to specify how it increments as well
for i in range(0, 11, 2):
	print(i)