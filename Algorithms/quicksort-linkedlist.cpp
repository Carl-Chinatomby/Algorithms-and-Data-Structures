/*
 * ***********************
 * By Carl Chinatomby
 * ***********************
 * CS220 Algorithsm - FALL 2009 - Prof. Brass - Section M
 * 
 * The task was to implement quicksort using linkedlists 
 * for the given function prototype and the given listnode 
 * definition. We were not allowed to copy the data into an 
 * array and sort that way. Must manipulate linked lists and 
 * pointers throughout the whole process. The pivot must also
 * be determined randomly at runtime.
 * 
 * Given prototypes:
 * struct listnode { int value; struct listnode *next;};
 * struct listnode *quicksort(struct listnode *data, int length);
 * 
*/
#include <iostream>
#include <ctime>
#include <cstdio>
#include <cstdlib>
using namespace std;

//This is the listnode definition that was given 
struct listnode { int value; struct listnode *next;};

//Inserts element to the head of the list
void list_head_insert(listnode*& head_ptr, int value, int& length){
	listnode* newnode = new listnode;	newnode->value=value;	newnode->next = head_ptr;
	head_ptr=newnode;
	length++;
}

//Removes an element from the list
void list_remove(listnode* previous_ptr, int& length){
	if (length > 0){
		listnode* remove = previous_ptr->next;
		previous_ptr -> next = previous_ptr->next->next;
		delete remove;
		length--;
	}
}

//Removes the head element of the list
void list_head_remove(listnode* &head_ptr, int& length){
	if (length > 0){
		listnode* remove = head_ptr;
		head_ptr = head_ptr->next;
		delete remove;
		length--;
	}
}

//Returns a pointer to the tail node of the list
listnode* findLastNode(listnode* head_ptr){
	listnode* last(NULL);
	if (head_ptr!=NULL)
		for (listnode* cursor=head_ptr; cursor!=NULL; cursor=cursor->next){
			if (cursor->next == NULL)
				last = cursor;
		}
	return last;
}


//returns a pointer to the sorted linked list - function prototype was given
struct listnode *quicksort(struct listnode *data, int length){
	listnode *pivot_ptr=NULL, *biggerList=NULL, *smaller_tail_ptr=data;

	if (length > 1){ 
		int pivotValue, pivotPosition = rand()%length+1, biggerLength(0);
		//first pass locate pivot
		listnode* cursor = data;
		for (int i=1; i <= pivotPosition; i++){
			if (i+1==pivotPosition || pivotPosition==1){ //if pivot is next or if pivot is first item
				pivot_ptr = new listnode; //create list of pivot alone
				pivot_ptr->value = cursor->next->value;
				pivot_ptr->next= cursor->next->next; 
				pivotValue = pivot_ptr->value;
				list_remove(cursor, length); //remove pivot from list
			}
			else
				cursor = cursor->next;
		}

		//partition list into two lists, smaller than and bigger than list

		//check nodes 2 to length
		for (cursor = data; cursor!=NULL; cursor = cursor->next) {
			while (cursor->next != NULL && cursor->next->value > pivotValue){
				list_head_insert(biggerList, cursor->next->value, biggerLength);
				list_remove(cursor, length);
			}
		}
		//Check Head Node
		if (data!= NULL && data-> value > pivotValue) {
			list_head_insert(biggerList, data->value, biggerLength);
			list_head_remove(data, length);
		}

		//recursive calls
		data=quicksort(data, length);

		if (length > 0){
			smaller_tail_ptr=findLastNode(data);
			smaller_tail_ptr->next=pivot_ptr;}
		else
			data=pivot_ptr;

		if (biggerLength > 0)
			pivot_ptr->next=quicksort(biggerList, biggerLength);
		else
			pivot_ptr->next=NULL;
	}
	return data;
}

int main(void)
{  /*
   This is the professor's test code
   Scores were either pass or fail if the test
   code succeeded and the program did not perform
   longer than O(nlogn)
   */
   int i;
   struct listnode *node, *tmpnode; node = NULL;
   for( i=0; i <100000; i++)
   { 
       tmpnode = node;
       node = (struct listnode *) malloc( sizeof(struct listnode));
       node->next = tmpnode; node->value = (29*i + 53124)%100000; 
   }
   printf("\n sorting \n");
   node = quicksort(node, 100000);
   tmpnode = node; i=0;
   while( tmpnode != NULL )
   { if (tmpnode->value != i )
     {  printf("sorting failed at i=%d\n", i);
        exit(0);
     }
     tmpnode = tmpnode->next; i = i+1;
   }
   printf("Sorting succeeded\n");
   exit(0);
}



