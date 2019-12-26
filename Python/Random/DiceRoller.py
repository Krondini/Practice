'''
Author: Konlan Rondini
Date: 12/26/19
Purpose: Short code to quickly roll dice for D&D characters
'''

from random import randint

def rollDice(num_dice, num_sides):
	
	result = []
	for i in range(num_dice):
		result.append(randint(1, num_sides))

	result = sorted(result, reverse=True)
	return result

def main():
	
	num_dice = int(input("Please enter how many dice you wish to roll: "))
	num_sides = int(input("Please enter how many sides these dice have: "))

	list_of_rolls = rollDice(num_dice, num_sides)

	print(list_of_rolls)

	return 0

if __name__ == '__main__':
	main()