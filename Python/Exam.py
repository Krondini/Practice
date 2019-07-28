def reverse_case(s):
	s2 = ""
	i = 0
	while i < len(s):
		check = s[i]
		if(check.islower() == True):
			s2 += check.upper()
			i += 1
		elif check.isupper() == True:
			s2 += check.lower()
			i += 1
		else:
			s2 += s[i]
			i += 1
	return s2

def main():
	x = reverse_case("Test Case")
	print(x)
	return 0

if __name__ == "__main__":
	main()