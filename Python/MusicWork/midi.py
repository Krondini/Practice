import py_midicsv
import sys

def main(argv):
	midi_fo = py_midicsv.midi_to_csv(argv[1]) #This is the midi file to convert
	for i in range(1000, 1100):
		print(midi_fo[i])

if __name__ == '__main__':
	main(sys.argv)