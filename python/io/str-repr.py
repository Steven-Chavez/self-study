# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 10/4/2017
# File: str-repr.py
# Resource: https://docs.python.org/3/tutorial/inputoutput.html

# str() and repr()
'''str() returns a human-readable representation of the 
values. repr() returns an interpreter-readable representation
of the values.'''

# Display differences between the two methods
s = "MAC address"
print(str(s))
print(repr(s))

# str.zfill() pads numeric strings with zeros on the left side.
i = 21
print(str(i).zfill(4))

