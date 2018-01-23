#! python3

''' root folder on windows C:\, linux /
Use strings to represent filepaths, and since windows uses \, you will have to
use \\ to represent \. ie C:\\spam\\folder\\path Or use rawstring r'C:\path\folder' 
'''

# the ever useful 'os' module that makes it so python program works on any OS

import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))
# this will print the path out correctly with \ or / depending on the OS

'''
os.join # takes several string arguments and combine it into a path
os.sep # os.join stores the new path into os.sep
os.getcwd() # gets the current working directory as a string function
os.chdir('c:\\newfilepath\folder\') # changes cwd
	^ should edit my tkinter mutombo gui.. now i know how to set relative filepath -_-
absolute filepath: c:\\spam\folder1\folder2\spam.png
relative filepath: spam.png... <- os will assume cwd as root folder
	so this is easier to change when programming (duh)
also, use '.\' dot-slash to refer to cwd (duh it's like that in limux)
'''
os.chdir('S:\\Desktop\\transfer\\')
print(os.getcwd())

# use abspath to change a relative path to absolute filepath
print(os.path.abspath('spam.png'))

# isabs check if path is absolute or not
os.path.isabs('..\\..\\spam.png')

# relpath - returns relative path from second entry to the 1st entry (starting point)
os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1')

os.path.dirname('S:\\Desktop\\transfer\\transferffff\\a.jpg') # will return only the dir
os.path.basename('S:\\Desktop\\transfer\\transferffff\\a.jpg') # will return the file

# check if path exists, return True or False
print(os.path.exists('c:\\folder1\\folder2\\spam.png'))
print(os.path.exists('c:\\windows\\system32\\calc.exe'))

# more os functions
print('Is it a file?')
print(os.path.isfile('S:\\Desktop\\transfer\\transferffff\\a.jpg'))
print('Is it a directory?')
print(os.path.isdir('S:\\Desktop\\transfer\\transferffff\\a.jpg'))
print('What is it\'s size?')
print(os.path.getsize('S:\\Desktop\\transfer\\transferffff\\a.jpg'))

# example code "Get total size of files in folder"

totalSize = 0
for filename in os.listdir('S:\\Pictures'):
	if not os.path.isfile(os.path.join('S:\\Pictures', filename)):
		continue
	totalSize = totalSize + os.path.getsize(os.path.join('S:\Pictures', filename))
print(totalSize)

# os.makedirs('c:\\food\\steaks\\filet\') , makes a folder