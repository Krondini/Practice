#include <iostream>
#include <cstring>
#include <cctype>

using namespace std;

bool owns_dog()
{
	bool dog = false;
	char ans[] = "";	
	printf("Do you own a dog?");
	cin >> ans;
	for(int i = 0; i < strlen(ans); i++)
	{
		putchar(tolower(ans[i]));
	}
	if(ans == "yes")
		dog = true;


	return dog;
}

void display_ad1(bool bool1)
{
	if(bool1){
		printf("Good, you have a dog.\n");
	}
	else{
		printf("Idiot has a cat.\n");
	}

}

int main(int argc, char const *argv[])
{
	bool does_own_dog = owns_dog();
	display_ad1(does_own_dog);

	return 0;
}