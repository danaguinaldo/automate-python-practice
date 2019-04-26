#! python3
# strongPassword.py - Test if password is strong.

import pyperclip, re

lengthRegex = re.compile(r'\w{7}(\w)+')
digitRegex = re.compile(r'\d+')
lowerRegex = re.compile(r'[a-z]+')
upperRegex = re.compile(r'[A-Z]+')

pw = input('Enter password:')

if lengthRegex.search(pw) == None:
    print("Password too short.")
elif digitRegex.search(pw) == None:
    print("Password requires at least one digit.")
elif lowerRegex.search(pw) == None:
    print("Password requires at least one lowercase letter.")
elif upperRegex.search(pw) == None:
    print("Password requires at least one uppercase letter.")
else:
    print("Password strength good!")