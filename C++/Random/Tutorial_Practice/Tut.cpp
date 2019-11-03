#include <cstdlib>
#include <iostream>
#include <string>
#include <limits>
#include <vector>
#include <sstream>
#include <numeric>
#include <ctime>
#include <cmath>

using namespace std;

int main(int argc, const char **argv)
{
	cout << "Please enter your age: ";
	string age;
	cin >> age;
	int nAge = stoi(age);

	bool ableToVote = (nAge >= 18) ? true : false;
	if(ableToVote)
		printf("You are able to vote!\n");
	else
		printf("You cannot vote yet!\n");

	int arrNums[10] = {1};
	for(int x: arrNums) cout << arrNums[x] << endl;

	return 0;
}