'''
def isPhoneNumber(text): # ie 415-555-
	if len(text) != 12:
		return False # not phone number size
	for i in range(0,3):
		if not text[i].isdecimal():
			return False # no area code
	if text[3] != '-':
		return False #missing dash
	for i in range(4,7):
		if not text[i].isdecimal():
			return False #no first 3 digits
	if text[7] != '-':
		return False #missing second dash
	for i in range(8,12):
		if not text[i].isdecimal():
			return False #missing last 4 digits
	return True

#holy cow, that's a lot of text above, just to check phone #
#(hint hint, use regex to make life easier)

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'
foundNumber = False
for i in range(len(message)):
	chunk = message[i:i+12] # manually scan each i in message for 12word chunks
	#it's nested in for i in range, so it will keep looping through whole message
	#searching for number, and running the isPhoneNumber def we defined above
	if isPhoneNumber(chunk): #look at a top where we defined isPhoneNumber def! wow, that does bulk of checking
		print('Phone number found: ' + chunk)
		foundNumber = True
if not foundNumber:
	print('Could not find any phone numbers.')
'''

#Above, not good. Regex, very good.
#below, Regex. Woot.

import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') #holy shit, it's like that?
#omg, I've used \d before, didn't know it's that easy in python. shiiiiiet.

mo = phoneNumRegex.search(message)
print(mo.group())

#holy. cow. 3 lines of code, instead of that huge blob up there.. WOW.
