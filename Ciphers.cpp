#include <iostream>

using namespace std;

string CaesarCipher(string input, int shift)
{
	string result = "";

	for(int i = 0; i < input.length(); i++)
	{
		if(isupper(input[i]))
			result += char(int(input[i]+shift-65)%26 + 65);
		else
			result += char(int(input[i]+shift-97)%26 + 97);
	}

	return result;
}

int main(int argc, char const *argv[])
{
	printf("Please input the word/phrase you wish to send\n");
	char input[100];
	cin.getline(input, sizeof(input));
	cout << "\n\n";
	int shift = stoi(argv[1]);
	cout << "Plaintext: " << input;
	printf("\nShift: %d\n", shift);
	cout << "Encrypted: " << CaesarCipher(input, shift) << endl;
	return 0;
}