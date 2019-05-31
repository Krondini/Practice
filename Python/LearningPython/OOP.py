from string import punctuation

class Example(object):
	"""docstring for Example"""
	def __init__(self, a, b):
		self.a = a
		self.b = b
	def add(self):
		return (self.a + self.b)

class Analyzer(object):
	"""docstring for Analyzer"""
	def __init__(self, s):
		for c in punctuation:
			s = s.replace(c, '')
		s = s.lower()
		self.words = s.split()
	
	def num_of_words(self):
		return len(self.words)
		

def main():
	x = Example(5, 3) #Creates new variable of type "Example"
	print(x.add()) #Invokes the function "add()" from within the Example class



if __name__ == '__main__':
	main()