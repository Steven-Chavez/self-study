# Author: Steven Chavez
# Email: steven@stevenscode.com
# Date: 9/20/2017
# File: dic.py
# Resource: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# Dictionaries
''' Dictionaries are usually seen in other languages as
as associative arrays. Dictionaries are made up of keys 
and values. Instead of indexes and values. Keys have to 
remain immutable. Keys have to remain unique per 
dictionary.'''

# Initialize basic dictionary
age = {'steven':27, 'jaky':26, 'tesla':1}
print(age)

# Add value to dictionary
age['breanna'] = 20
print(age)

# Delete value in dictionary
del age['jaky']
print(age)

# Convert dictionary keys to list
ageList = list(age.keys())
print(ageList)

# Sort keys from dictionary to list
ageSort = sorted(age.keys())
print(ageSort)

# Search for key in list
boolean = 'tesla' in age
print(boolean)

# Looping techniques
'''Use the items() methods to retrieve keys and values'''
for i, j in age.items():
    print(i, j)

