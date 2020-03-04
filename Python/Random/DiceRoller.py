'''
Author: Konlan Rondini
Date: 12/26/19
Purpose: Short code to quickly roll dice for D&D characters
'''

from random import randint
from sys import argv

def rollDice(num_dice, num_sides):
	
	result = []
	for i in range(num_dice):
		result.append(randint(2, num_sides))

	result = sorted(result, reverse=True)

	return result

def main(args):
	
	char_roll = input("Is this a character roll? (y/n) ")

	if char_roll.lower() == 'n': #Random roll
		num_dice = int(input("Please enter how many dice you wish to roll: "))
		num_sides = int(input("Please enter how many sides these dice have: "))

		list_of_rolls = rollDice(num_dice, num_sides)

		print(list_of_rolls)

	else: #Character roll
		six_rolls = []
		for i in range(6):
		
			new_roll = rollDice(4, 6)
			del new_roll[-1]
			roll_sum = sum(new_roll)
			six_rolls.append(roll_sum)

		six_rolls = sorted(six_rolls, reverse=True)

		print(six_rolls)


	return 0

if __name__ == '__main__':
	main(argv)