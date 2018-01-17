#! python

'''regex continued, other regex.py getting too long
quick review, re.compile has .search() and .findall()
Like word processor, re also has "find and replace"
'''

import re

namesRegex = re.compile(r'W\w+')
song = 'In the song "Recipe" by Kendrick Lamar ft Dre, they sang about the 3W\'s. Women, Weed, and Weather.'
print(namesRegex.findall(song, re.VERBOSE))
print(namesRegex.sub('KEEP IT PG!', song))
