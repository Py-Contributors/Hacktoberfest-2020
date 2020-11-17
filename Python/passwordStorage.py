#! python3
#pw.py - An insecure password locker program
#This program saves password's of accounts in the form of a dictionary.

#Add password to the dictionary when needs to be updated.
pwd = {'email': 'afnoiariwrniwriPOIARIIFJ',
'blog': 'SujJUUbKBP8293hHU79hsis',
'luggage': '10000000001212'}

import sys,pyperclip
if len(sys.argv)<2:
    print('Please enter the account as parameter along with running the program')
    sys.exit()

account=sys.argv[1]

if account in pwd:
    pyperclip.copy(pwd[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('the account does not exist'+ account)
