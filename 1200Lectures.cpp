/*
Cat Rondini
1200 Lectures (in C/C++)
*/

#include <iostream>
#include <cmath>

using namespace std;

int calculate_song_storage(float GB)
{
	float size_in_MB = GB * 1024;
	size_in_MB /= 3.5;
	return floor(size_in_MB);
}

int main(int argc, char const *argv[])
{
	float MP3_size = stof(argv[1]);
	int num_songs = calculate_song_storage(MP3_size);
	printf("You can store %d songs on this MP3.\n", num_songs);
	// cout << "The address of the variable 'MP3_size' is: " << &MP3_size << endl;
	return 0;
}