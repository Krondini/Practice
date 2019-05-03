#include <iostream>
#include <fstream>
#include <cctype>
#include <cstdlib>
#include <ctime>
#include <vector>

using namespace std;

void menu()
{
	cout << "\nPlease select which type of cipher " 
		 <<"you would like to use: \n";
	printf("1.) Caesar Cipher\n");
	printf("2.) Vigenere Cipher\n");
	printf("3.) Hill/Matrix Cipher\n");
	printf("0.) Exit\n");
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
				result += char(int(input[i]+shift-65)%25 + 65);
			else
				result += char(int(input[i]+shift-97)%25 + 97);	
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
	string result = "";

	//Building the encryption table
	for (int i = 0; i < 26; ++i)
	{
		for (int j = 0; j < 26; ++j)
			EncryptTable[i][j] = char(65+(i+j)%25);
	}

	for (int i = 0; i < input.length(); ++i)
	{
		if(input[i] != char(32))
		{
			char newChar = EncryptTable[int(input[i])%25][int((key[i])%key.length())%25];
			result += newChar;
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

string HillCipher(string input, int size)
{
	//Number of dimensions in the plaintext vector
	int dimSize = input.length();

	//Declare Matrix
	int EncryptMatrix[dimSize][dimSize];
	
	//Initialize matrix values
	srand((unsigned)time(0));
	for(int i = 0; i < dimSize; i++) 
	{
		for(int j = 0; j < dimSize; j++)
			EncryptMatrix[i][j] = (rand()%1000)+1;
	}
	
	for(int i = 0; i < dimSize; i++) 
	{
		for(int j = 0; j < dimSize; j++)
			printf("%d\n", EncryptMatrix[i][j]);
	}
	//Convert plaintext to uppercase
	for(int i = 0; i < dimSize; i++)
		input[i] = toupper(input[i]);
	string result = "";

	//Add ASCII values to plaintext vector
	int charVals[dimSize];
	for (int i = 0; i < dimSize; i++)
	{
		charVals[i] = int(input[i]%25);
		printf("%d\n", charVals[i]);
	}

	//Encrypted vector to decode from
	int resultVec[dimSize];
	for (int i = 0; i < dimSize; ++i)
		resultVec[i] = 0;

	//Multiply plaintext vector with Encryption Matrix
	for(int j = 0; j < dimSize; j++)
	{
		for(int i = 0; i < dimSize; i++)
		{
			resultVec[j] += (EncryptMatrix[i][j]*charVals[j]);
		}
		resultVec[j] = (resultVec[j]%25) + 65;
	}

	for(int i = 0; i < dimSize; i++)
	{
		result += char(resultVec[i]);	
	}

	return result;
}

/* Takes in a file name
* Decodes a file with several encoded message
* Returns the original plaintext
*/
string Decoder(string filename)
{
	ifstream fo;
	fo.open(filename);
	char data[100];

	fo >> data; //Read first line
}

int main(int argc, char const *argv[])
{

	printf("Please input the word/phrase you wish to send\n");
	string input;
	getline(cin, input);
	//cout << "Input is: " << input << endl;

	ofstream fo;
	fo.open("CodesToDecode.txt", ofstream::app);
	cout << "\n\n";
	int choice = -1;
	while(choice != 0)
	{
		menu();
		cin >> choice;
		if(choice == 1) //Caesar Cipher
		{
			cout << "Please enter how far you would like to "
				 << "shift your message\n";
			int shift;
			cin >> shift;
			string Encrypted = CaesarCipher(input, shift);
			cout << "Plaintext: " << input;
			printf("\nShift: %d\n", shift);
			cout << "Encrypted: " << Encrypted << endl;
			fo << Encrypted << endl;
		}
		else if(choice == 2) //Vigenere Cipher
		{
			printf("Please enter your key word:\n");
			string key;
			cin >> key;
			string Encrypted = VigenereCipher(input, key);
			cout << "\n\nPlaintext: " << input;
			cout << "\nKey: " << key;
			cout << "\nEncrypted: " << Encrypted << endl;
			fo << Encrypted << endl;
		}
		else if(choice == 3) //Matrix Cipher
		{
			string Encrypted = HillCipher(input, input.length());
			cout << "\n\nPlaintext: " << input;
			cout << "\nSize of Matrix: " << input.length() 
			<< 'x' << input.length();
			cout << "\nEncrypted: " << Encrypted << endl;
			fo << Encrypted << endl;
		}
	}
	fo.close();
	return 0;
}