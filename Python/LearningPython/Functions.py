import random
import os
import math

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

def first_diff(str1, str2):
	if(str1 == str2):
		return -1
	else:
		i = 0
		for i in range(len(str1)):
			if(str1[i] != str2[i]):
				return i+1
			else:
				continue
		return i+1

def binom(n, k):
	#binomial coefficient defined as (n!/(k!*(n-k)!))
	return (math.factorial(n)/(math.factorial(k)*(math.factorial(n-k))))

def main():
	#Task 1
	n_rectangle = int(input("Please enter the number of rows\nfor function 'rectangle': "))
	m_rectangle = int(input("Please enter the number of columns\nfor function 'rectangle': "))
	os.system("clear")
	print("Here is a %dx%d rectangle:"%(n_rectangle,m_rectangle))
	rectangle(n_rectangle,m_rectangle)
	
	while True:
		waiting = input("> ")
		if waiting == "":break
	os.system("clear")

	#Task 2
	list_of_strings = []
	while True:
		print("If you would like to exit, enter ''")
		new_item = input("Please enter a string: ")
		if(new_item == ''):
			break
		list_of_strings.append(new_item)
	os.system("clear")

	print("Before: ", end='')
	print(list_of_strings)

	list_of_strings = addExcitement(list_of_strings)
	
	print("\nAfter: ", end='')
	print(list_of_strings)

	while True:
		waiting = input("> ")
		if waiting == "":break
	os.system("clear")

	#Task 3
	n_digitalRoot = int(input("Please enter a number to find the Digital Root of: "))
	answer = digitalRoot(n_digitalRoot)
	os.system("clear")
	
	print("Digital Root of %d is: %d" % (n_digitalRoot,answer))
	while True:
		waiting = input("> ")
		if waiting == "":break
	os.system("clear")

	#Task 4
	str1 = input("Please enter the first string to check: ")
	str2 = input("\nPlease enter the second string to check: ")
	os.system("clear")

	diff_check = first_diff(str1, str2)
	if(diff_check == -1):
		print("The strings are exactly the same!")
	else:
		print("The strings differ at position %d" % diff_check)

	while True:
		waiting = input("> ")
		if waiting == "":break
	os.system("clear")

	#Task 5
	print("Calculating binomial coefficient: ")
	int1 = int(input("Please enter the first integer n: "))
	int2 = int(input("Please enter the second integer k: "))
	os.system("clear")

	binom_coeff = binom(int1, int2)
	print("Binomial Coefficient for %d and %d is: %d" % (int1, int2, binom_coeff))

	while True:
		waiting = input("> ")
		if waiting == "":break
	os.system("clear")

	return 0

if __name__ == '__main__':
	main()