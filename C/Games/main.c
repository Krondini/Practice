#include <stdio.h>
#include "Nim.h"

int menu()
{
	short int choice;
	printf("Please enter which game you would like to play:\n");
	printf("1. Nim\n");
	scanf("%hu", &choice);

	return choice;
}

int main(int argc, char const *argv[])
{
	short int choice = menu();
	if (choice == 1) {nimGame();}
	fflush(stdout);
	return 0;
}