#! python

''' parsing text! woohoo. plaintext files. Other files like doc, pdf, html are
"BINARY FILES"
'''

# "File" data type
helloFile = open('S:\\Desktop\\transfer\\automatetheboringstuff\\hello.txt')
content = helloFile.read() # returns a single string
print(content)
helloFile.close() # don't know why, but if I don't close and open file again, readlines() won't work
# can only read file content once, if need to read it again have to open it again
helloFile = open('S:\\Desktop\\transfer\\automatetheboringstuff\\hello.txt')
content = helloFile.readlines() # returns a list of strings
print(content)

''' to edit the file, need to open it in 'write' mode, but it will overwrite the file
to add to the end of file, use 'append' mode by adding 'a' to the end. 
helloFile = open('S:\\Desktop\\transfer\\automatetheboringstuff\\hello.txt', 'a')
'write' mode use 'w'
If file doesn't exist, python will create a new blank file
'''
helloFile = open('S:\\Desktop\\transfer\\automatetheboringstuff\\hello2.txt', 'w')
helloFile.write('That\'s what Billy Joel said.')
helloFile.write('Achoooooooooo')
helloFile.write('Achoooooooooo')
helloFile.write('Achoooooooooo')
helloFile.write('Achoooooooooo')
helloFile.close()

''' checked text file, see that it does not add \n newline char -_-, when using 
'write' have to manually add it
'''
baconFile = open('bacon.txt', 'w')
baconFile.write('Bacon is not a vegetable')
baconFile.close()
# where is the file? use os.getcwd() to find it

baconFile = open('bacon.txt', 'a')
baconFile.write('\n\nBacon is delicious, but so is Tofu. And Tofu is healthy.. halp')
baconFile.close()

''' write and close text file is useful for single strings, but complex variables
need to use shelve. it's like a dictionary
'''

# shelve, it's like a dictionary
import shelve
shelfFile = shelve.open('mydata')
shelfFile['cats'] = ['Zophie', 'Pookie', 'Snowflake', 'Kendrick', 'Dre', 'Dogg']
shelfFile.close()

shelfFile = shelve.open('mydata')
cats = shelfFile['cats']
print(cats)

# check your dir, shelve created couple of dictionary binary files (mydata.bak)