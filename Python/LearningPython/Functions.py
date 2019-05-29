import random

def rectangle(n,m):
	for rows in range(n):
		for cols in range(m):
			print('*',end='')
		print('')

def addExcitement1(list_of_strings):
	for item in list_of_strings:
		item += '!'
	return list_of_strings

def main():
	#Task 1
	n_rectangle = int(input("Please enter the number of rows\nfor function 'rectangle': "))
	m_rectangle = int(input("Please enter the number of columns\nfor function 'rectangle': "))
	rectangle(n_rectangle,m_rectangle)

	#Task 2
	list_of_strings = []
	while True:
		print("If you would like to exit, enter '0'")
		new_item = input("Please enter a string: ")
		if(new_item == '0'):
			break
		list_of_strings.append(new_item)

	print("Before: ", end='')
	print(list_of_strings)
	list_of_strings = addExcitement1(list_of_strings)
	print("\nAfter: ", end='')
	print(list_of_strings)
	return 0

if __name__ == '__main__':
	main()