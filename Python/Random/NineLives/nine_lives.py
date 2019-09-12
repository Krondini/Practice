import random
import sys
import os

'''
Function takes in an integer as the difficulty of the word
1 = 'Easy', 2 = 'Medium', 3 = 'Hard'
Each difficulty corresponds to a different set of words
Set of words is read in from a text file and populates the list from main()
'''
def populateList(difficulty):
	list_words = []

	while True:
		if(difficulty == 1):
			# list_words.append('1')
			fo = open("EasyWords.txt", 'r')
			for line in fo:
				line = line.strip()
				list_words.append(line)

			fo.close()
			break

		elif(difficulty == 2):
			# list_words.append('2')
			fo = open("MediumWords.txt", 'r')
			for line in fo:
				line = line.strip()
				list_words.append(line)

			fo.close()
			break

		elif(difficulty == 3):
			# list_words.append('3')
			fo = open("HardWords.txt", 'r')
			for line in fo:
				line = line.strip()
				list_words.append(line)

			fo.close()
			break

		else:
			difficulty = int(input("Please insert a valid difficulty: "))

	return list_words

def runGame(chosen_word):
	list_rep = []
	num_lives = 9

	for i in range(len(chosen_word)): list_rep.append('')
	
	print("Your word is: %s" % list_rep)
	guess_letter = ''
	while (num_lives != 0) and (list_rep != chosen_word):
		#begin loop for player
		guess_letter = input("Please enter a guess for the word:\n> ")
		while(not guess_letter.isalpha()):
			guess_letter = input("Please enter a guess for the word:\n> ")
		
		if guess_letter in chosen_word:
			#Replace spot in list_rep with letter
			print("%s is in the word!" % guess_letter)
			break #Remove these breaks later to have game work

		else:
			num_lives -= 1
			print("Sorry, your guess was wrong!")

		if num_lives == 0:
			print("Out of lives, you lose!")
			break

		



def main(argv):
	
	potential_words = [] #populated by different words
	difficulty = int(input("Please enter your desired difficulty: "))
	potential_words = populateList(difficulty)
	
	os.system('clear')
	print("List of words is: \n")
	print(potential_words)
	input('> ')

	os.system('clear')
	
	chosen_word = potential_words[random.randint(0, len(potential_words)-1)]
	runGame(chosen_word)


if __name__ == '__main__':
	main(sys.argv)