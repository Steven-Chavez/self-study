# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/7/2017
# File: break_continue.py
# Resource: https://docs.python.org/3/tutorial/controlflow.html

'''
The break statment breaks out of the loop. keeping the loop
from finishing
'''
for n in range(2, 11):
	print('n = ' + str(n))
	for m in range(2, 11):
		print('m = ' + str(m))
		if (n + m) % 2 == 0:
			print('break')
			break
else: 	# when used with loop else has more in common with try
	print("else")