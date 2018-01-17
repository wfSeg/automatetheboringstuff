#! python3

#regex is insane
import re

phoneRegex = re.compile(r'((\d\d\d\-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 408-555-1234,777-8888,222-555-1212')
phone = mo.group()
print(phone)


digit = '1234567890'
print('number of digits: ' + digit)
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search(digit)
print('Regex object search(?) match minimum 3 to maximum of 5 #\'s ' + mo.group())
digitRegex = re.compile(r'(\d){3,5}?') # ? after the {} does a none greedy match
mo = digitRegex.search(digit)
print('? after {} does a non greedy match, so default to minimum 3 #\'s ' + mo.group())


#findall regex
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
resume = """'Berkeley Faculty numbers '510-642-0237', '510-643-8435',
'510-643-6633', '510-642-1728', '510-642-6506', '510-642-9945',
'510-642-9423'"""

print('This is search result: ' + str(phoneRegex.search(resume))) #re.search only shows first match
print('This is findall result: ' + str(phoneRegex.findall(resume))) #re.findall shows all matches

'''findall only returns strings if there's 0-1 group in regex
but if the regex object has 2 or more groups, it will return a list of tuples
of strings'''

#putting it all to use in an xmas song
import pprint
lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, and 1 partridge in a pear tree'

xmasRegex = re.compile(r'\d+\s\w+')
pprint.pprint(xmasRegex.findall(lyrics))

'''make your own char class
like this regexObj = re.compile(r'[]')'''
vowelRegex = re.compile(r'[aeiou]') # shorter than r'(a|e|i|o|u)'
#can specify a range r'[a-z]' or r'[a-zA-Z]
print(vowelRegex.findall('Robocop eats babyfood'))
doubleVowelRegex = re.compile(r'[aeiouAEIOU]{2}')
print(doubleVowelRegex.findall('Robocop eats babyfood'))
vowelRegex = re.compile(r'[^aeiou]') #find consonants instead
print(vowelRegex.findall('Robocop eats babyfood'))
vowelRegex = re.compile(r'[^aeiou\s]') #this will also not match spaces
print(vowelRegex.findall('Robocop eats babyfood'))

#dot 
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
#this returns all _at, but flat is returned as lat
atRegex = re.compile(r'.{1,2}at')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
'''this returns _cat, _hat, flat. flat is fixed, but now it has space in front of
cat, hat, mat etc
atRegex = re.compile(r'(.*at)')
print(atRegex.findall('The cat in the hat sat on the flat mat.'))
'''

#dot stahh
name = 'First Name: Stephen Last Name: Curry'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(nameRegex.findall(name))

#non greedy vs greedy
serve = '<To serve humans> for dinner.>'
nongreedy = re.compile(r'<(.*?)>')
print(nongreedy.findall(serve))
greedy = re.compile(r'<(.*)>')
print(greedy.findall(serve))
''' .* is greedy, in 'serve' there is <text>text>, it matches < then scan for > but
it sees > text >, it matches the latter >. If you use .*?, it's nongreedy,
it scans 'serve' for < then sees > text >, and matches first > only and skip text
after first >.'''

prime = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
print(prime)

dotStar = re.compile(r'.*')
print(dotStar.search(prime))
#it matches everything, except newline. To get newline, use re.DOTALL
dotStar = re.compile(r'.*', re.DOTALL)
print(dotStar.search(prime))

#now we have replace feature
namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob')
print(mo) #prints out Agents name
# the re.sub method replaces text in B with those in A ('A', 'B')
redacted = namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob')
print(redacted)

# (\w)\w* will only return ['A', 'B']
namesRegex = re.compile(r'Agent (\w)\w*') # only has 1st initial
# \1 <- will only show first part of matched string?
redacted = namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob')
print(redacted)

# Verbose format, it allows you to use ''' triple quotes to ident and comment within the regex!
#easier to read
re.compile(r'''
	(\d\d\d-)| 		# area code
	(\(\d\d\d\) )   # -or- area code with parens and no dash
	\d\d\d    	# first 3 digits
	-			# second dash
	\d\d\d\d    # last 4 digits
	\sx\d{2,4}  # extension, like x1234''', re.VERBOSE)
