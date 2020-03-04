#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include "Nim.h"

void nimGame(void)
{
	bool p1_turn = true;
	short int curr_score = 20;

	printf("Do you want to play against the computer? (y/n): ");
	char temp;
	scanf("%c", &temp);
	bool comp_game = (temp == 'y') ? true : false;

	//If two player game
	if(!comp_game)
	{
		char p1_name[20];
		char p2_name[20];
		printf("Player 1, please enter your name: ");
		scanf("%s", p1_name);
		printf("Player 2, please enter your name: ");
		scanf("%s", p2_name);
		//Proceed with game until score reaches 0 

		printf("Number of tokens to begin with: %hu\n\n", curr_score);
		while(curr_score > 0)
		{
			short int num;
			printf("%s, enter a number between 1 and 3: ", p1_name);
			scanf("%hu", &num);
			curr_score -= num;

			if(curr_score <= 0) {break;}
			p1_turn = !p1_turn;
			printf("Number of tokens left: %hu\n\n", curr_score);

			printf("%s, enter a number between 1 and 3: ", p2_name);
			scanf("%hu", &num);
			curr_score -= num;

			if(curr_score <= 0) {break;}
			p1_turn = !p1_turn;
			printf("Number of tokens left: %hu\n\n", curr_score);
		}

		//Outcome of game
		if(p1_turn) {printf("%s wins, congratulations!\n", p1_name);}\
		else{printf("%s wins, congratulations!\n", p2_name);}
	}	
	else
	{
		char p1_name[20];
		printf("Human player, please enter your name: ");
		scanf("%s", p1_name);
		short int num;
		printf("%s will be playing against the computer.\n", p1_name);

		while(curr_score > 0)
		{
			printf("%s please choose a number between 1 and 3: ", p1_name);
			scanf("%hu", &num);
			curr_score -= num;
			printf("Number of tokens left: %hu\n\n", curr_score);

			printf("Computer will now take %d tokens: \n", (4 - num));
			curr_score -= (4 - num);
			printf("Number of tokens left: %hu\n\n", curr_score);
		}
		printf("Computer wins, so sorry %s\n", p1_name);
	}
}