#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
	int age = 30;
	double gpa = 3.14;
	char grade = 'A';

	printf("Memory address of 'Age': %p\n", &age);
	printf("Memory address of 'GPA': %p\n", &gpa);
	printf("Memory address of 'Grade': %p\n", &grade);

	return 0;
}