#! python3

''' delete files using os.unlink(), delete directory using os.rmdir()
there's also shutil.rmtree('c:\\delicious')
'''

import os

print(os.getcwd())
os.chdir('S:\\Pictures')

for filename in os.listdir('S:\\Pictures'):
	if filename.endswith('.jpg'):
		# os.unlink(filename) <- example of 'dry run', comment out delete codes
		print(filename)		# safer to print out list of files to delete

# even safer to use 'send2trash' module (install it with pip)

import send2trash

send2trash.send2trash('S:\\Desktop\\transfer\\automatetheboringstuff\\importantfile.txt')
