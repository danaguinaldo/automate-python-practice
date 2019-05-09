#! python3
# madlib.py - Create a story with user input.

import re, os

madlibRegex = re.compile(r'(ADJECTIVE)|(NOUN)|(VERB)|(ADVERB)')

#TODO: Read File
madTextFile = open("./madlib/madlib.txt", 'r')
madText = madTextFile.read()
madTextFile.close()

#TODO: Match ADJ, NOUN, VERB, ADVERB
while re.search(madlibRegex, madText) != None:
    if re.search(madlibRegex, madText).group() == 'ADJECTIVE':
        adj = input("Enter an adjective: ")
        madText = re.sub(madlibRegex, adj, madText, 1)
    elif re.search(madlibRegex, madText).group() == 'NOUN':
        noun = input("Enter a noun: ")
        madText = re.sub(madlibRegex, noun, madText, 1)
    elif re.search(madlibRegex, madText).group() == 'VERB':
        verb = input("Enter a verb: ")
        madText = re.sub(madlibRegex, verb, madText, 1)
    elif re.search(madlibRegex, madText).group() == 'ADVERB':
        adverb = input("Enter an adverb: ")
        madText = re.sub(madlibRegex, adverb, madText, 1)

#TODO: Write to file
madTextFile = open("./madlib/madlib.txt", 'w')
madTextFile.write(madText)
madTextFile.close()