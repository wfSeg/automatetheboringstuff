#! python3

# making your own exception statements, instead of try

"""

*************
*			*
*			*
*			*
*************

"""

def boxPrint(symbol, width, height):
	print()
	print(symbol * width)

	for i in range (height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)

	print(symbol * width)

boxPrint('*', 15, 5)

boxPrint('+', 10, 8)
