#! python3
# strip.py - Imitate the strip function with Regex

import re

text = input("Enter text to strip: ")
stripChar = input("Enter character to strip (Default is space): ")
strippedText = None

def strip(text, strippedChar):
    if strippedChar == '':
        stripRegex = re.compile(r'^\s+|\s+$')
        strippedText = stripRegex.sub('', text)
        return strippedText
    else:
        stripRegex = re.compile(r'{}+|{}+$'.format(strippedChar, strippedChar))
        strippedText = stripRegex.sub('', strip(text, ''))
        return strippedText

print(strip(text, stripChar))