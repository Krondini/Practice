#include <iostream>
#include <fstream>
#include <ctime>
#include <cmath>
#include <iomanip>

using namespace std;

double mySqrt(double num1){
	return sqrt(num1);
}

int main(int argc, char* argv[])
{
	system("clear");
	cout << "Testing mySqrt()\n\n";

	const char separator = ' '; //variables to be used for formatting
	const int nameWidth  = 10;

	cout << left 
		 << setw(nameWidth) << "|Original Number "
		 << setw(nameWidth) << "|Sqaure Root"
		 << endl;

	int sqrt0 = mySqrt(4);
	int sqrt1 = mySqrt(12.25);
	int sqrt2 = mySqrt(0.0121);

	cout << left
		 << setw(nameWidth) << "|4"
		 << setw(nameWidth) << '|' << sqrt0
		 << endl;

	cout << left
		 << setw(nameWidth) << "|12.25"
		 << setw(nameWidth) << '|' << sqrt1
		 << endl;

	cout << left
		 << setw(nameWidth) << "|0.0121"
		 << setw(nameWidth) << '|' << sqrt2
		 << endl;

	int list_nums[100];
	string choice;
	printf("Now enter your own numbers:\nEnter 'z' when finished");
	while(choice != 'z')
	{
		if(choice)
	}


	return 0;
}