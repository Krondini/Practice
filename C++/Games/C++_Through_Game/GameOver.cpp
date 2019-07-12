#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char* argv[])
{
	system("clear");
	cout << "Game Over!\n";
	cin.get();

	system("clear");
	vector<string> inventory;
	try{
		inventory[0] = "Sword";
		cout << inventory[0];
	}
	catch(exception& fault){
		cerr << "Exception caught: " << fault.what() << endl;
	}

	cin.get();
	return 0;
}