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

agents = 'Agent Alice, Agent Smith, and Agent Wendy met up with Agent Bob to talk about Agent Agent'
namesRegex = re.compile(r'Agent (\w)\w*')
print(namesRegex.findall(agents))
print(namesRegex.sub(r'Agent \1****', agents))

print('How many times does Selena Gomez sings "To get to you" in the song "Wolves"?')
lyrics = '''
In your eyes, there's a heavy blue
One to love and one to lose
Sweet divide, a heavy truth
Water or wine, don't make me choose

I wanna feel the way that we did that summer night (night)
Drunk on a feeling, alone with the stars in the sky

I've been running through the jungle
I've been running with the wolves
To get to you, to get to you
I've been down the darkest alleys
Saw the dark side of the moon
To get to you, to get to you
I've looked for love in every stranger
Took too much to ease the anger
All for you, yeah, all for you
I've been running through the jungle
I've been crying with the wolves
To get to you, to get to you (oh to get to you)

Your fingertips trace my skin
To places I have never been
Blindly I am following
Break down these walls and come on in

I wanna feel the way that we did that summer night
Drunk on a feeling, alone with the stars in the sky

I've been running through the jungle
I've been running with the wolves
To get to you, to get to you
I've been down the darkest alleys
Saw the dark side of the moon
To get to you, to get to you
I've looked for love in every stranger
Took too much to ease the anger
All for you, yeah, all for you
I've been running through the jungle
I've been crying with the wolves
To get to you, to get to you (oh to get to you)

I've been running through the jungle
I've been running with the wolves
To get to you, to get to you
I've been down the darkest alleys
Saw the dark side of the moon
To get to you, to get to you
I've looked for love in every stranger
Took too much to ease the anger
All for you, yeah, all for you
I've been running through the jungle
I've been crying with the wolves
To get to you, to get to you (oh to get to you)'''

lyricsRegex = re.compile(r'To get to you', re.IGNORECASE) 
print(lyricsRegex.findall(lyrics))
print('She sang it ' + str(len(lyricsRegex.findall(lyrics))) + ' times')

#Today is Wednesday, it's Hump Day. I'm in a hump.. wait no. I'm in a slump.
#ugh. 

