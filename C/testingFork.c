#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

int main(int argc, char const *argv[])
{
	int ret1 = fork();
	int ret2 = fork();
	int ret3 = fork();


	
	if(!ret1 && !ret2 && ret3)
		printf("World\n");


	sleep(1);
	return 0;
}