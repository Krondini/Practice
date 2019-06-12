#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cstdlib>
#include <ctime>

using namespace std;

void playGame(string str)
{
	int word_length = str.length();
	int tries = 0;

	string result = string(word_length, '-');

	cout << "Your word is " << result << endl;
	while(result != str && tries != 10)
	{
		char guess = ' ';
		cout << "Please guess a letter: ";
		cin >> guess;
		size_t found = str.find(guess);
		
		if(found == string::npos)
		{
			tries++;
			cout << "Your guess is not in the word\n";
		}

		int find_letter = 0; //Iterator to find letter
		
		while(tries < 10) //Replace result string with correct letter
		{
			bool letter_flag = false;

			while(str[find_letter] != guess)
				find_letter++;

			if(find_letter < str.length())
			{
				result[find_letter] = guess;
				find_letter++;
				letter_flag = true;
			}

			if(!letter_flag)
			{
				cout << "You have " << 10-tries << " tries remaining\n";
				break;
			}
		}
		cout << "Your word is " << result << endl;
	}

	system("clear");
	if(tries != 10)
		cout << "You win!!\n";
	else
		cout << "You lose, GAME OVER!\n";

	return;
}

int main(int argc, char const *argv[])
{
	vector<string> possible_words;
	srand ( unsigned (time(0)) );

	string line = "";
	ifstream readFile ("HangmanWords.txt");

	if(!readFile.is_open()) //Unable to open file
	{
		cout << "There was an error opening the file, "
			 << "ending program!\n";
		return -1;
	}
	else //Reading in file
	{
		while(getline(readFile, line))
			possible_words.push_back(line);

		readFile.close();
	}

	system("clear");
	random_shuffle(possible_words.begin(), possible_words.end());
	playGame(possible_words[0]);

	cin.get();

	return 0;
}