#include <iostream>
#include <ctime>
using namespace std;

struct listnode { int value; struct listnode *next;};

void list_head_insert(listnode*& head_ptr, int value, int& length){
	listnode* newnode = new listnode;
	newnode->value=value;
	newnode->next = head_ptr;
	head_ptr=newnode;
	length++;
}

void list_remove(listnode* previous_ptr, int& length){
	if (previous_ptr!= NULL){
		listnode* remove = previous_ptr->next;
		previous_ptr -> next = previous_ptr->next->next;
		delete remove;
		length--;
	}
}




void list_head_remove(listnode* &head_ptr, int& length){
	if (head_ptr != NULL){
		listnode* remove = head_ptr;
		head_ptr = head_ptr->next;
		delete remove;
		length--;
	}
}

void print(listnode* head_ptr)
{
	if (head_ptr!=NULL)
		for (listnode* cursor=head_ptr; cursor!=NULL; cursor=cursor->next){
			cout << cursor -> value << " ";
		}
	cout << endl;
	cout << endl;
}

struct listnode *quicksort(struct listnode *data, int length){
	listnode *pivot_ptr=NULL, *biggerList=NULL, *smaller_tail_ptr=data;
	if (length > 1){
		int pivotValue, pivotPosition = rand()%length+1, biggerLength(0);


		//first pass locate pivot
		listnode* cursor = data;
		for (int i=1; i <= pivotPosition; i++){
			if (i+1==pivotPosition || pivotPosition==1){
				pivot_ptr = new listnode;
				pivot_ptr->value = cursor->next->value;
				pivot_ptr->next= cursor->next->next; 

				pivotValue = pivot_ptr->value;
				cout << "Pivot Value is: " << pivotValue << endl;
				list_remove(cursor, length);
			}
			else
				cursor = cursor->next;
		}//for

		//partition list into two lists, smaller than and bigger than list

		//check nodes 2 to length
		for (cursor = data; cursor!=NULL && cursor->next != NULL; cursor = cursor->next) {

			while (cursor->next != NULL && cursor->next->value > pivotValue){
				list_head_insert(biggerList, cursor->next->value, biggerLength);
				list_remove(cursor, length);
			}
			if (cursor->next== NULL)
				smaller_tail_ptr = cursor;
		}
		//Check Head Node
		if (data!= NULL && data-> value > pivotValue) {
			list_head_insert(biggerList, data->value, biggerLength);
			list_head_remove(data, length);
		}

		cout << "Printing Smaller List" << endl;
		print(data);
		cout << "Printer Bigger List" << endl;
		print(biggerList);


		//recursive calls

		data=quicksort(data, length);
		smaller_tail_ptr->next = pivot_ptr;
		pivot_ptr->next=quicksort(biggerList, biggerLength);


/*
		cout << "Sorting SMALLER LIST!!!" << endl;
		


		cout << "Sorting BIGGER LIST!!!" << endl;
//		quicksort(pivot_ptr->next, biggerLength);
		
		
		quicksort(biggerList, biggerLength);

		//combine
		
		
		if (biggerList !=NULL)
			pivot_ptr->next = biggerList;
		
*/
		cout << "PRINTING MERGED LIST" << endl;
		print(data);
	}//if
	return data;
}//quicksort

int main()
{
	const int CAPACITY = 10;
	listnode* head_ptr = NULL;
	int length(0);

	srand(time(NULL));

//	quicksort (head_ptr,length); // sort empty list
//	cout << endl;

	for (int i=0; i<CAPACITY; i++){
		list_head_insert(head_ptr, rand()%CAPACITY, length);
	}

	for (listnode* cursor=head_ptr; cursor!=NULL; cursor=cursor->next){
		cout << cursor -> value << " ";
	}
	cout << endl;

	quicksort(head_ptr, length);

	for (listnode* cursor=head_ptr; cursor!=NULL; cursor=cursor->next){
		cout << cursor -> value << " ";
	}
	cout << endl;

}
