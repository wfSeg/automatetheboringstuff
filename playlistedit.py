#! python3
# so playlist from my pc has E: drive, but work pc is using G: drive, replace it using regex?
'''
playlistFile = open('G:\\sleeping - Copy.fpl')
content = playlistFile.read()
print(content)
'''

playlistFile = open('G:\\sleeping.fpl', 'r') # using 'r' read tag

'''
filedata = filedata.replace('E:', 'G:') # this will change E: to G:.. BUT!

# it will also replace 'file:' to 'filG:' <- do another replace
filedata = filedata.replace('filG', 'file') # there's gotta be a better way to do this

# probably with regex. Yes most likely with regex

content = playlistFile.read()
playlistFile.close()
newcontent = content.replace('E:','G:')
playlistFile = open('newplaylistoutput', 'w')
playlistFile.write(newcontent)
playlistFile.close()

well... this 'worked' kind of, the output is in current working directory,
so had to locate it, and then it didn't have proper extension .fpl, add it. But
when tried to open it, corrupted output ha. Guess python just save it as plaintext
'''
import os
os.chdir('G:\\')

content = playlistFile.read()
playlistFile.close()
newcontent = content.replace('E:','G:')
playlistFile = open('newplaylistoutput.fpl', 'w')
playlistFile.write(newcontent)
playlistFile.close()

''' yeah.. got directory right, but file still 'corrupted', even though save with
.fpl extension. Foobar is giving me this 
"The following error(s) occurred during loading of the location(s):
Unsupported format or corrupted file"
'''

