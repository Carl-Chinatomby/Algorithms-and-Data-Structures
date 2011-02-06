//Carl Chinatomby - CS220 Algorithms - FALL 2009 - Prof. Brass - Section M
#include <iostream>
#include <ctime>
using namespace std;

struct listnode { int value; struct listnode *next;};

void list_head_insert(listnode*& head_ptr, int value, int& length){
	listnode* newnode = new listnode;	newnode->value=value;	newnode->next = head_ptr;
	head_ptr=newnode;
	length++;
}

void list_remove(listnode* previous_ptr, int& length){
	if (length > 0){
		listnode* remove = previous_ptr->next;
		previous_ptr -> next = previous_ptr->next->next;
		delete remove;
		length--;
	}
}

void list_head_remove(listnode* &head_ptr, int& length){
	if (length > 0){
		listnode* remove = head_ptr;
		head_ptr = head_ptr->next;
		delete remove;
		length--;
	}
}

listnode* findLastNode(listnode* head_ptr){
	listnode* last(NULL);
	if (head_ptr!=NULL)
		for (listnode* cursor=head_ptr; cursor!=NULL; cursor=cursor->next){
			if (cursor->next == NULL)
				last = cursor;
		}
	return last;
}
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
		}//for

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
	}//if
	return data;
}//quicksort


int main()
{
	const int CAPACITY = 100;
	listnode* head_ptr = NULL;
	int length(0);

	srand(time(NULL));

	quicksort (head_ptr,length); // sort empty list
	cout << endl;

	for (int i=0; i<CAPACITY; i++){
		list_head_insert(head_ptr, rand()%CAPACITY, length);
	}

	for (listnode* cursor=head_ptr; cursor!=NULL; cursor=cursor->next){
		cout << cursor -> value << " ";
	}
	cout << endl;

	head_ptr=quicksort(head_ptr, length);

	for (listnode* cursor=head_ptr; cursor!=NULL; cursor=cursor->next){
		cout << cursor -> value << " ";
	}
	cout << endl;

}
