import sys
import math

def pythagorean(a, b):
	return pow((a**2 + b**2), (1/2))

def my_math(x, y):
	ans = int(x) - int(y)
	print(" x - y is " + str(ans))

def main(args):
	for i in range(1, len(args)):
		args[i] = int(args[i])
	my_math(args[1], args[2])
	c = pythagorean(int(args[1]), int(args[2]))
	print(" c of %d and %d is: %d" % (int(args[1]), int(args[2]), c))

	return 0

if __name__ == '__main__':
	try:
		finish = main(sys.argv)
	except Exception as e:
		raise e
	
	print("Program finished with execution code: %d" % (finish))
