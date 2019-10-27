#include <stdio.h>
#include <stdlib.h>

float convertAmounts(float conversion){

}

int main(int argc, char const *argv[])
{
	char char_cupcakes[8];
	printf("Please enter how many cupcakes you would like to make: ");
	scanf("%s", char_cupcakes);
	int num_cupcakes = atoi(char_cupcakes);

	printf("\n%d cupcakes!\n", num_cupcakes);
	return 0;
}