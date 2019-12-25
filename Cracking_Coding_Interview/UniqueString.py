from sys import argv
from string import ascii_uppercase

def checkUnique(letter, dict_letters):
	if dict_letters[letter] > 1: return False
	else: return True

def main(args):
	
	string_to_check = args[1].upper()
	dict_letters = {}
	for i in ascii_uppercase:
		dict_letters[i] = 0

	for letter in string_to_check:
		dict_letters[letter] += 1
		if(not checkUnique(letter, dict_letters)):
			print("The string has repeated the letter %s" % letter)
			return False

	print("No repeated letters")

	return True

if __name__ == '__main__':
	main(argv)