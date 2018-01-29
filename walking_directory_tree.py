#! python3

''' I'm on lesson 34 now yay. Walking a directory tree, like SNMP walk.
instead of manually writing a program, use os.walk() module! 
'''

import os

dir = os.walk('S:\\Desktop\\transfer\\automatetheboringstuff\\delicious')
print(dir)

''' doesn't work, because os.walk returns THREE values used in 'for' loops
example:
for a, b, c in dir:
	print('the folder is ' + a)
	print('the subfolders in ' + a + ' are: ' + str(b))
	print(c)
'''
for folderName, subfolders, filenames in dir:
	print('The folder is ' + folderName)
	print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
	print('The filenames in ' + folderName + ' are:\n' + str(filenames))
	print()

	for subfolder in subfolders:
		print(subfolder)
		#or delete subfolders with 'fish' in its name
		if 'fish' in subfolder:
			# os.rmdir(subfolder) <- dry run it
			print('rmdir on ' + subfolder)

	for file in filenames:
		if file.endswith('.py')
			shutil.copy(os.join(foldername, file), os.join(folderName, file + '.backup'))
