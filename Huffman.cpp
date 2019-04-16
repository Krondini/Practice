#include <iostream>
#include <cstdlib>

using namespace std;

/* This constant can be avoided by 
*  Calculating explicit height of tree
*/
#define MAX_TREE_HEIGHT 100

struct minHeapNode{
	char data; //Label for node

	unsigned frequency; //Frequency of character

	struct minHeapNode *left, *right; //Children of node
};

struct minHeap{
	unsigned size; //Current size of heap

	unsigned capacity; //Capacity of min heap

	struct minHeapNode** arr;
};

struct minHeapNode* newNode(char data, unsigned frequency)
{
	struct minHeapNode* temp
		= (struct minHeapNode*)malloc(sizeof(struct minHeapNode));
	temp->left = temp->right = NULL;
	temp->data = data;
	temp->frequency = frequency;

	return temp;
}

struct minHeap* createMinHeap(unsigned capacity)
{
	struct minHeap* minHeap
		= (struct minHeap*)malloc(sizeof(struct minHeap));
	minHeap->size = 0;
	minHeap->capacity = capacity;

	minHeap->arr
		= (struct minHeapNode**)malloc(minHeap->
		capacity * sizeof(struct minHeapNode*));
		return minHeap;
}

void swapMinHeapNode(struct minHeapNode** a,
					 struct minHeapNode** b)
{

	struct minHeapNode* t = *a;
	*a = *b;
	*b = t;
}

void minHeapify(struct minHeap* minHeap, int index)
{

	int smallest = index;
	int left = 2*index+1;
	int right = 2*index+2;

	if(left < minHeap->size && minHeap->arr[left]->
		frequency < minHeap->arr[smallest]->frequency)
		smallest = right;
	if(smallest != index){
		swapMinHeapNode(&minHeap->arr[smallest],
						&minHeap->arr[index]);
		minHeapify(minHeap, smallest);
	}
}

int isSizeOne(struct minHeap* minHeap)
{
	return (minHeap->size == 1);
}

struct minHeapNode* extractMin(struct minHeap* minHeap)
{
	struct minHeapNode* temp = minHeap->arr[0];
	minHeap->arr[0]
		= minHeap->arr[minHeap->size - 1];

	minHeap->size--;
	minHeapify(minHeap, 0);

	return temp;
}



int main(int argc, char const *argv[])
{
	/* code */
	return 0;
}