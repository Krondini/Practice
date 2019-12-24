#include <iostream>

using namespace std;

void FizzBuzz(int input)
{
	for(int i = 1; i <= input; i++)
	{
		bool test_mod_3 = ((i%3) == 0) ? true : false;
		bool test_mod_5 = ((i%5) == 0) ? true : false;

		if(test_mod_3)
			cout << "Fizz";
		if(test_mod_5)
			cout << "Buzz";

		if(!test_mod_5 && !test_mod_3)
			cout << i;

		cout << endl;
	}
}

int main(int argc, char const *argv[])
{
	int num_time = stoi(argv[1]);

	FizzBuzz(num_time);
	return 0;
}