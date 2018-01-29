#! python3

'''sh util, shutil.
'''

import shutil

shutil.copy('c:\\spam.txt', 'c:\\delicious\\spamspamspam.txt')

# copies whole directory tree
#shutil.copytree('c:\\delicious', 'c:\\delicious_backup')

shutil.move('c:\spam.txt', 'c:\\delicious\\walnut')
