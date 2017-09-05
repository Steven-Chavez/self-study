# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/4/2017
# File: strings.py

''' Strings can be in closed with single quotes '..'
or with double quotes "..". What you decide to use is
up to you there is no difference. Use \ to escape. '''

print('doesn\'t') # escape single quote with \'
print("doesn't") # if you use double quotes escaping is unessary

# newline \n
print("Hello\nGoodbye")

# raw strings doesn't display newline when \n is used
print(r'C:\user\ninja')

# String literals ("""...""") are used to cover multiple lines
print("""
String Literals
	can cover multiple lines            -n
	formated and displayed as written   -w
""")