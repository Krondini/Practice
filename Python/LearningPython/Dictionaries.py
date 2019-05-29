import random

def createDeck():
	deck = [{'value':i, 'suit':c}
			for c in['Hearts', 'Diamonds', 'Clubs', 'Spades']
			for i in range(2,15)]
	return deck

def main():
	#Simple manipulation/learning Dicts
	test_dict = {'A':100, 'B':200}
	print("Entire dictionary is: ")
	for entry in test_dict:
		print("\t%s: %d"%(entry, test_dict[entry]))
	print("\nFirst we have test_dict[A]: %d"%test_dict['A'])
	test_dict['A'] = 400
	print("Next we have test_dict[A]: %d\n"%test_dict['A'])
	test_dict['C'] = 500
	print("After adding a new entry:")
	for entry in test_dict:
		print("\t%s: %d"%(entry, test_dict[entry]))
	del test_dict['A']
	print("\nNow after deleting an entry:")
	for entry in test_dict:
		print("\t%s: %d"%(entry, test_dict[entry]))
	print("\n\n")
	
	#Testing creating a deck of cards
	newDeck = createDeck()
	for card in newDeck:
		if(card['value'] == 11):
			card['value'] = 'Jack'
		elif(card['value'] == 12):
			card['value'] = 'Queen'
		elif(card['value'] == 13):
			card['value'] = 'King'
		elif(card['value'] == 14):
			card['value'] = 'Ace'

	for i in range(10):
		random.shuffle(newDeck)
	for card in newDeck:
		print(str(card['value']) + ' of ' + card['suit'])
	# print("Hello World")

if __name__ == '__main__':
	main()