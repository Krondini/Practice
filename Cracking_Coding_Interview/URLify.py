from sys import argv

def URLify(string):
	
	new_string = ""
	for i in range(len(string)):
		
		if ord(string[i]) == 32:
			new_string += "%20"
			while string[i] != " ":
				pass
		
		else: new_string += string[i]


	return new_string

def main(args):
	
	string_to_check = input("Please enter a phrase: ")
	print("Original string: %s" % string_to_check)
	new_string = URLify(string_to_check)
	print("New string: %s" % new_string)


if __name__ == '__main__':
	main(argv)