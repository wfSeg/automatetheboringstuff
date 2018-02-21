#! python3

# example use of assertion, with simple traffic light program
# example: assert False, 'This is the error message'

market_2nd = {'ns': 'green', 'ew': 'red'} # dictionary structure

def switchLights(intersection):
	for key in intersection.keys():
		if intersection[key] == 'green':
			intersection[key] = 'yellow'
		elif intersection[key] == 'yellow':
			intersection[key] = 'red'
		elif intersection[key] == 'red':
			intersection[key] = 'green'
	assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)

print('test done')
