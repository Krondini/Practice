#include <stdio.h>

void print_name(char name[]){
	printf("Hello %s!\n", name);
}

void print_hello(){
	printf("Hello World!\n");
}

int main(){
	print_hello();
	char name[20];
	printf("Please enter your name: ");
	scanf("%s", name);

	print_name(name);
	return 0;
}