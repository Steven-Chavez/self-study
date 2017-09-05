# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/4/2017
# File: strings.py

''' Strings can be in closed with single quotes '..'
or with double quotes "..". What you decide to use is
up to you there is no difference. Use \ to escape. '''

print('doesn\'t') # escape single quote with \'
print("doesn't") # if you use double quotes escaping is unnecessary

# newline \n
print("Hello\nGoodbye")

# raw strings doesn't display newline when \n is used
print(r'C:\user\ninja')

# String literals ("""...""") are used to cover multiple lines.
# \ prevents automatic end of lines
print("""\
String Literals
	can cover multiple lines            -n
	formatted and displayed as written   -w\
""")

# String concatenation using + 
name = 'Steven' + ' ' + 'Chavez'
print(name)

# Repeat operator (*) repeats string 
name = 3 * name
print(name) #name is displayed 3 times

''' Automatic concatenation occurs when two string 
literals are next to each other. Does not work when 
you use a variable a and a literal. An error occurs '''
name = 'Steven' ' ' 'Chavez'
print(name)

# particularly useful in cases like this
print("Program or be programed\n"
	  "Author: Douglas Rushkoff")