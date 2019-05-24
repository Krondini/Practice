import numpy
import matplotlib
import sys
from operator import itemgetter

class VG(object):
	Rank = 1
	Name = 2
	Genre = 3
	ESRB = 4
	Platform = 5
	Publisher = 6
	Developer = 7
	Crit_Score = 8
	User_Score = 9
	Total_Shipped = 10
	Global_Sales = 11
	NA_Sales = 12
	PAL_Sales = 13
	JP_Sales = 14
	Other_Sales = 15
	Year = 16

def sortLL(dataset, column):
	sorted(dataset, key=itemgetter(int(column)))
	return dataset

def organizeData(dataset):
	print("Please enter how you wish to ")
	print("organize the dataset\n")
	print("{}".format("\t1.) By Name"))
	print("{}".format("\t2.) By Year Released"))
	print("{}".format("\t3.) By ESRB Rating"))
	print("{}".format("\t4.) By Genre"))
	print("{}".format("\t5.) By Platform"))
	org_choice = -1
	while((type(org_choice) != int) or (org_choice < 1 or org_choice > 5)):
		org_choice = int(input('> '))
	if org_choice == 1:
		sortLL(dataset, 0)
	elif org_choice == 2:
		sortLL(dataset, 1)
	elif org_choice == 3:
		sortLL(dataset, 2)
	elif

def readFile(filename):
	fo = open(filename, 'r')
	header = fo.readline() #obtain header line
	list_of_lines = [] #list to return
	for line in fo:
		line = line.strip().split(',')
		list_of_lines.append(line)

		fo.readline() #move to next line
	return list_of_lines

def main(argv):
	# print("Temp") Testing
	# print(argv[1]) Testing
	dataset = readFile(argv[1])
	if not dataset:
		print("Dataset is empty, ending program!")
		return -1
	organizeData(dataset)

	return 0

if __name__ == '__main__':
	main(sys.argv)