import sys

def parseStatement(filename):
	fo = open(filename, 'r')
	line = fo.readline() #Skip header
	line = fo.readline() #First line of actual data
	amounts = []


	while line:
		amounts.append(line[3])
		line = fo.readline()

def main(argv):
	# print("Hello")
	parseStatement(argv)

if __name__ == '__main__':
	main(sys.argv[1])