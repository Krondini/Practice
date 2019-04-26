#include <iostream>
#include <cctype>

using namespace std;

void menu()
{
	cout << "\nPlease select which type of cipher " 
		 <<"you would like to use: \n";
	printf("1.) Caesar Cipher\n");
	printf("2.) Vigenere Cipher\n");
	printf("0.) Exit\n");

	return;
}


/* Function takes in a string input and an integer to shift by
* And shifts all letters in the message by the shift int
*/
string CaesarCipher(string input, int shift)
{
	string result = "";

	for(int i = 0; i < input.length(); i++)
	{
		if(input[i] != char(32))
		{
			if(isupper(input[i]))
				result += char(int(input[i]+shift-65)%26 + 65);
			else
				result += char(int(input[i]+shift-97)%26 + 97);	
		}
		else
			result += input[i];
	}

	return result;
}


/* Function takes in a two strings: an input and a key
* And encrypts the message by shifting letters based on the 
* Given key word
*/
string VigenereCipher(string input, string key)
{
	char EncryptTable[26][26];
	for (int i = 0; i < input.length(); ++i)
		input[i] = toupper(input[i]);
	cout << input << endl;
	string result = "";

	//Building the encryption table
	for (int i = 0; i < 26; ++i)
	{
		for (int j = 0; j < 26; ++j)
			EncryptTable[i][j] = char(65+(i+j)%26);
	}

	for (int i = 0; i < input.length(); ++i)
	{
		if(input[i] != char(32))
		{
			char newChar = EncryptTable[]
		}
		else
			result += char(32);
	}
	// for (int i = 0; i < 26; ++i)
	// {
	// 	for (int j = 0; j < 26; ++j)
	// 		cout << EncryptTable[i][j];
	// 	cout << "\n";
	// }

	return result;
}

int main(int argc, char const *argv[])
{

	printf("Please input the word/phrase you wish to send\n");
	char input[100];
	cin.getline(input, sizeof(input));
	cout << "\n\n";
	int choice = -1;
	while(choice != 0)
	{
		menu();
		cin >> choice;
		if(choice == 1)
		{
			cout << "Please enter how far you would like to "
				 << "shift your message\n";
			int shift;
			cin >> shift;
			cout << "Plaintext: " << input;
			printf("\nShift: %d\n", shift);
			cout << "Encrypted: " << CaesarCipher(input, shift) << endl;			
		}
		else if(choice == 2)
		{
			printf("Please enter your key word:\n");
			string key;
			cin >> key;
			VigenereCipher(input, key);
		}
	}

	return 0;
}