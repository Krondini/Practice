import numpy as np
import sys

def sigmoid(x):
	return (1/(1+np.exp(-x)))

def neural(in1, in2, w1, w2, bias):
	out = (w1*in1) + (w2*in2) + bias
	return sigmoid(z)

def main(argv):
	print(argv[0])
	test_in1 = np.random.randn()
	test_in1 = 

if __name__ == '__main__':
	main(sys.argv)