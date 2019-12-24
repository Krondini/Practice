#include <iostream>
#include <vector>

using namespace std;

unsigned long int Pell(int n)
{
	if((n == 0) || (n == 1))
		return 1;
	else
		return (2*Pell(n-1) + Pell(n-2));
}

/*
unsigned long int memoPell(int n, std::vector<unsigned long int> Arr)
{
	if((n == 0) || (n == 1))
		return 1;

	else if(find(Arr.begin(), Arr.end()) == Arr[n])
		return Arr[n];

	else{
		unsigned long int new_num = (2*Pell(n-1) + Pell(n-2));
		Arr.push_back(new_num);
		return 	new_num;
	}
}
*/

unsigned long int iterPell(int n)
{
	auto Pell1 = 1;
	auto Pell2 = 1;
	unsigned long int new_Pell;
	for(int i = 2; i <= n; i++)
	{
		new_Pell = (2*Pell1 + Pell2);
		Pell1 = Pell2;
		Pell2 = new_Pell;
		printf("The %dth Pell number is: %lu\n", i, new_Pell);
	}

	return new_Pell;
}

int main(int argc, char const *argv[])
{
	short int num_Pell = stoi(argv[1]);
	std::vector<unsigned long int> v;


	unsigned long int new_num = iterPell(num_Pell);
	

	return 0;
}