import sys

def adjusted(recipe_mult, og_amt, units, name):
	new_amt = og_amt*recipe_mult
	return ("You need %f %s of %s" % (new_amt, units, name))

def main(args):
	for i in range(1, len(args)):
		args[i] = int(args[i])
	num_cake = args[1]
	recipe_mult = num_cake/12
	amt_flour = 100.0
	amt_sugar = 100.0
	num_eggs = 1.0
	new_flour = adjusted(recipe_mult, amt_flour, 'grams', 'flour')
	new_sugar = adjusted(recipe_mult, amt_sugar, 'grams', 'sugar')
	new_eggs = adjusted(recipe_mult, num_eggs, 'units', 'egss')
	print(new_flour + '\n' + new_sugar + '\n' + new_eggs)

if __name__ == '__main__':
	main(sys.argv)