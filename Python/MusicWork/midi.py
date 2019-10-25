import py_midicsv
import sys

def main(argv):
	midi_fo = py_midicsv.midi_to_csv(argv[1]) #This is the midi file to convert
	for line in midi_fo:
		line = line.strip().split(", ")
		print(line)


if __name__ == '__main__':
	main(sys.argv)