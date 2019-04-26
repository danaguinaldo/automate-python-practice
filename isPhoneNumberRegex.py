#! python3 
# isPhoneNumberRegex.py - Find phone number with regex

import re

# Regular Regex
# Curly Brackets ({}) match specific repetitions
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNumRegex.search('My number is 415-555-4242.') 
print('Phone number found: ' + mo.group())
print('')

# Matched Groups
print("Groups:")
phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415-555-4242.') 
print('group(): ' + mo.group())
print('group(0): ' + mo.group(0))
print('group(1): ' + mo.group(1))
print('group(2): ' + mo.group(2))
print('')

# Working with Pipes (OR)
print("Pipes (|):")
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.') # Get's the first match
print('Batman and Tina Fey: ' + mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.') 
print('Tina Fey and Batman: ' + mo2.group())
print('')

# Optional Match with Question Mark (?)
print('Option Match with Question Mark (?):')
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The Adventures of Batman')
print('The Adventures of Batman: ' + mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print('The Adventures of Batwoman: ' + mo2.group())
print('')

# Zero or More with Asterisk (*)
print("Zero or More with Asterisk (*):")
batRegex1 = re.compile(r'Bat(wo)*man')
mo1 = batRegex1.search('The Adventures of Batman')
print('The Adventures of Batman: ' + mo1.group())
mo2 = batRegex1.search('The Adventures of Batwoman')
print('The Adventures of Batwoman: ' + mo2.group())
mo3 = batRegex1.search('The Adventures of Batwowowowoman')
print('The Adventures of Batwowowowoman: ' + mo3.group())
print('')

# One or More with Plus (+)
print("One or More with Plus (+):")
batRegex2 = re.compile(r'Bat(wo)+man')
mo1 = batRegex2.search('The Adventures of Batman')
print('mo1 == None: ' + str(mo1 == None))
mo2 = batRegex2.search('The Adventures of Batwoman')
print('The Adventures of Batwoman: ' + mo2.group())
mo3 = batRegex2.search('The Adventures of Batwowowowoman')
print('The Adventures of Batwowowowoman: ' + mo3.group())
print('')

# Find All Method
print('Find All Method:')
print(phoneNumRegex.findall('My number is 415-555-4242. His number is 281-330-8004'))
print('')

# Character classes
print('Character Classes:')
xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge') )
print('')

# Creating Your Own Character Classes
print('Own Character Class:')
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
print('')

print('Negative Character Class:')
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))
print('')

# Beginning and End with Caret and Dollar Sign (^, $)
print("Begin and End with Caret (^):")
beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello world!')
print('Hello world!: ' + str(mo1 != None))
print('')

print('Ends with Dollar Sign ($):')
endsWithNumber = re.compile(r'\d$')
mo1 = endsWithNumber.search('Your number is 42')
print('Your number is 42: ' + str(mo1 != None))
print('')

# Match Everything with Dot (.)
print('Match Everything with Dot (.):')
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Danny Last Name: Aguinaldo')
print('group(1): ' + mo.group(1))
print('group(2): ' + mo.group(2))
print('')

# Match Everything with Dot Including Newline
print('No Newlines:')
noNewLineRegex = re.compile('.*')
mo = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())
print('')

print('Newlines:')
newlineRegex = re.compile('.*', re.DOTALL)
mo = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo.group())
print('')

# Ignore Case - Use re.IGNORECASE / re.I
print('Ignore Case:')
robocop = re.compile(r'robocop', re.I)
mo = robocop.search('RoboCop is part man, part machine, all cop.')
mo1 = robocop.search('ROBOCOP protects the innocent.')
mo2 = robocop.search('Al, why does your programming book talk about robocop so much?')
print('RoboCop is part man, part machine, all cop.: ' + mo.group())
print('ROBOCOP protects the innocent.: ' + mo1.group())
print('Al, why does your programming book talk about robocop so much?: ' + mo2.group())