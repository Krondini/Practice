from sys import argv
from string import ascii_uppercase, ascii_lowercase


'''
Take two strings to compare against each other
Create a dictionary for each string
Add up the counts of each letter, if the two counts are equal then the two are permutations
'''
def main(args):

	str1 = args[1]
	str2 = args[2]
	count1 = 0
	count2 = 0

	dict_str1 = {}

	#Create the dictionaries
	counter = 1
	for i in ascii_lowercase:
		dict_str1[i] = counter
		counter += 1

	for i in ascii_uppercase:
		dict_str1[i] = counter
		counter += 1

	#Count up letters
	for i in str1:
		count1 += dict_str1[i]

	for i in str2:
		count2 += dict_str1[i]

	if count1 == count2:
		print("The two strings are permutations")
		return True

	else:
		print("The two strings are NOT permutations")
		return False

if __name__ == '__main__':
	main(argv)

