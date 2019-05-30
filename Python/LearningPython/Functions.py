import random

def rectangle(n,m):
	for rows in range(n):
		for cols in range(m):
			print('*',end='')
		print('')

def addExcitement(list_of_strings):
	for item in range(len(list_of_strings)):
		list_of_strings[item] += '!'
	return list_of_strings

def digitalRoot(n):
	if len(str(n)) == 1:
		return n
	answer = 0
	for digit in str(n):
		answer += int(digit)
	return digitalRoot(answer)

def main():
	#Task 1
	n_rectangle = int(input("Please enter the number of rows\nfor function 'rectangle': "))
	m_rectangle = int(input("Please enter the number of columns\nfor function 'rectangle': "))
	rectangle(n_rectangle,m_rectangle)
	print('')

	#Task 2
	list_of_strings = []
	while True:
		print("If you would like to exit, enter ''")
		new_item = input("Please enter a string: ")
		if(new_item == ''):
			break
		list_of_strings.append(new_item)

	print("Before: ", end='')
	print(list_of_strings)

	list_of_strings = addExcitement(list_of_strings)
	
	print("\nAfter: ", end='')
	print(list_of_strings)

	#Task 3
	n_digitalRoot = int(input("Please enter a number to find the Digital Root of: "))
	answer = digitalRoot(n_digitalRoot)
	
	print("Digital Root of %d is: %d" % (n_digitalRoot,answer))


	return 0

if __name__ == '__main__':
	main()