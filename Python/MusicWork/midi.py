import py_midicsv
import sys
import numpy as np

def main(argv):
	midi_fo = py_midicsv.midi_to_csv(argv[1]) #This is the midi file to convert
	for line in midi_fo:
		line = line.strip().split(", ")
		print(line)


	image_data = np.genfromtxt("image_data.csv", delimiter=',')
	

if __name__ == '__main__':
	main(sys.argv)