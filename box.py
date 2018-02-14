#! python3

# making your own exception statements, instead of try

"""

*************
*			*
*			*
*			*
*************

use traceback and assert
"""

def boxPrint(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('"symbol" needs to be a string of length 1')
	if (width < 2) or (height < 2):
		raise Exception('"width" and "height" must be >= 2')
	print()
	print(symbol * width)

	for i in range (height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)

	print(symbol * width)

boxPrint('*', 15, 5)

boxPrint('+', 10, 8)
# examples of "traceback"
#boxPrint('++', 5, 10)
#boxPrint('O', 1, 1)

''' traceback module and traceback formatting
'''

import traceback
try:
	raise Exception('This is the error message')
except:
	errorFile = open('error_log.txt', 'a')
	errorFile.write(traceback.format_exc())
	errorFile.close()
	print('The traceback info was written to error_log.txt')