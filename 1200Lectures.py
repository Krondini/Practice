'''
Cat Rondini
CSCI 1200 Lectures (in Python)
'''
import sys
import math

def calculate_song_storage(GB):
	size_in_MB = GB * 1024
	size_in_MB /= 3.5

	return math.floor(size_in_MB)

def main(argv):
	MP3_size = float(argv[1])
	MP3_size = int(calculate_song_storage(MP3_size))
	print(MP3_size)

if __name__ == '__main__':
	main(sys.argv)