# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/22/2017
# File: modules.py
# Resource:https://docs.python.org/3/tutorial/modules.htm://docs.python.org/3/tutorial/modules.html

# Modules
''' A module is a file. This file contains Python statements
and definitions.'''

# In order to use other module functions you import the modue
import header

# By using the module name you can access the functions.
header = header.display('Steven', 'S@yahoo.com', 'Sept 22, 2017')

# dir() function is used to find out which names a module defines
print(dir(header))
print(dir())
print()

# List the built in function using builtins
import builtins
print(dir(builtins))