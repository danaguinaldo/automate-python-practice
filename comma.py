#! python3
# comma.py - Format sentence with list.

spam = ['apples', 'bananas', 'tofu', 'cats']
spam1 = ['Enen', 'Joka', 'Mia', 'Courtney', 'Josh', 'Jan', 'Justin']

def comma(spamList):
    print(', '.join(spamList[0:-1]) + ' and ' + spamList[-1])

def main():
    comma(spam1)

main()