#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	char *str = (char*)(malloc(sizeof(char) * 6));
	str[0] = 'H';
	str[1] = 'e';
	str[2] = 'l';
	str[3] = 'l';
	str[4] = 'o';
	str[5] = '\0';

	char str2[6] = "World";

	printf("%s\n", str);
	printf("%s\n", str2);
	return 0;
}