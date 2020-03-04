import sys
import csv

'''
Takes in a potential prime 'num'
Finds all numbers which evenly divide into 'num'
If there is a unique factor besides 1 and the number itself, function returns flase
Else function returns true
'''
def isPrime(num):
	#Trivial cases
	if(num == 2) or (num == 5):
		return True
	if(num == 1):
		return False

	for i in range(2, num-1):
		if(num % i == 0):
			return False
	return True

def main(argv):
	list_of_primes = []

	for i in range(1, int(argv[1])):
		if(isPrime(i)):
			list_of_primes.append(i)

	with open("List_of_primes.csv", 'w', newline='') as csvfile:
		write = csv.writer(csvfile, delimiter=',')
		
		write.writerow(list_of_primes)

	return 0

if __name__ == '__main__':
	main(sys.argv)