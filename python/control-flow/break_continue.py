# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/7/2017
# File: break_continue.py
# Resource: https://docs.python.org/3/tutorial/controlflow.html

'''
The break statment breaks out of the loop. In the example below
the nested for statement never gets past the first iteration
because the break statement is called.
'''
for n in range(1, 11):
	print('n = ' + str(n))
	for m in range(1, 11):
		print('m = ' + str(m))
		if n % m == 0:
			print('break')
			break
else:
	print("else")