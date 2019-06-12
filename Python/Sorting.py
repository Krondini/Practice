import sys

def menu():
	print("Please select which sort you want to perform")
	print("1.) Bubble Sort")
	print("2.) Selection Sort")
	print("0.) Exit")

'''
Simple Bubble Sort method
Ascending order
'''
def bubbleSort(lst):
	for num1 in range(0, len(lst)):
		for num2 in range(num1+1, len(lst)):
			if lst[num1] > lst[num2]: #Swaps numbers
				temp = lst[num1]
				lst[num1] = lst[num2]
				lst[num2] = temp

	return lst

def selectionSort(lst):
	new_lst = []

'''
Reads in a file and stores the numbers/words
into a list to be sorted later
'''
def parseFile(filename):
	num_list = []
	fo = open(filename, 'r')
	for line in fo:
		line = line.strip().split(',')
		# num_list.append(line)
		for num in line: 
			if num.isnumeric(): num_list.append(int(num))
			else: num_list.append(num)

	return num_list

def main(args):
	num_to_sort = parseFile(args[1])
	choice = -1
	menu()
	choice = int(input())
	if choice == 1:
		num_to_sort = bubbleSort(num_to_sort)
	elif choice == 2:
		num_to_sort = selectionSort(num_to_sort)
	print(num_to_sort)

	print("Goodbye") #Ending statement

if __name__ == '__main__':
	main(sys.argv)