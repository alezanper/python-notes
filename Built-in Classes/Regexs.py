import re

noMatch = re.match('^[A-Za-z]+$', 'Hello3')
print(noMatch)

match = re.match('^[A-Za-z]+$', 'Hello')
print(match)

#Checking for numbers
match = re.match('^[\d]+$', '32')
print(match)

#Checking for letters
match = re.match('^[A-Za-zÑñ]+$', 'Alex')
print(match)

#Checking for special characters
match = re.match('^[\ \.\,\:\$\%\&]+$', '.,:')
print(match)