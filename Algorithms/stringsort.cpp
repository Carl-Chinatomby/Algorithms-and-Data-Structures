/*
*******************
By Carl Chinatomby
*******************
Fall 2009 Algoriths Morning Section Tues/Thurs
HW#2 - String Sort Using BucketSort Algorithm

Assignment: 

Write code that sorts a set of words (strings) give as linked
list. This list is declared by the following nodes:

struct listnode { struct listnode * next;
                  char * word; } ;

The strings are '\0'-terminated strings (char arrays), as usual
in C. The function has the following declration:

struct listnode *stringsort(struct listnode *data);

The function should be a wrapper function for the following 
ssort that does the real work, by recursive bucketsort.

struct front_back *ssort(struct front_back *data, int next)

The function needs to recieve pointers to front and end of the
list, and returns such a pointer pair, when the list is sorted.
The function ssort gets an additional integer argument next; it
assumes that the strings on the input list are all having the same
letters up to position next - 1. It hten performs bucketsort 
according to the letter at position next and calls itself 
recursively for the position next+1 on each bucket that contains
more than one item. After that, the list in each nonempty bucket
are sorted, and still need to be linked together, using the pointers
to the back of each list. After that, the linked-together list is 
sorted. The function ssort retunrns this list. 


*/
#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

struct listnode { struct listnode * next;
                  char * word; } ;

struct front_back { listnode* front; listnode* back;};


struct front_back *ssort(struct front_back *data, int next)
{
	const int SIZE = 127;
	int i,j; front_back bucket[SIZE]; front_back *subbucket; listnode *cursor;
	
	for(i=0; i<SIZE; i++) {bucket[i].front = NULL; bucket[i].back = NULL;} //set all to NULL

	cursor = data->front;
	while (cursor != NULL){
		if (cursor->word[next] != '\0') {
			listnode* newnode =  new listnode; newnode->word = cursor->word; newnode->next = bucket[cursor->word[next]].front; bucket[cursor->word[next]].front=newnode; //head insert into bucket
			if (bucket[cursor->word[next]].front->next == NULL)	{	bucket[cursor->word[next]].back = bucket[cursor->word[next]].front;	} //front = back if only 1 node
			cursor = cursor->next;
		}
	}
	//recursive calls
	for (i=0; i<SIZE; i++){	if (bucket[i].front != NULL && bucket[i].front != bucket[i].back) {	subbucket = ssort(&bucket[i], next+1);	bucket[i]=*subbucket;	}}

	//delete data (since we only head insert and didn't remove)
	while (data->front !=NULL) { listnode* remove = data->front; data->front = data->front->next; delete remove; }

	//merge step
	for (j=0; bucket[j].front == NULL;j++){}	data=&bucket[j]; 	listnode *prevTail = bucket[j].back; //find the first non empty bucket (start) and locate its tailpointer
	for (i=j+1; i<SIZE; i++)	{	if (bucket[i].front != NULL){	prevTail->next = bucket[i].front;	prevTail = bucket[i].back;		}} //connect tail to front of next bucket
	data->back = prevTail; //update tail pointer of completed list

	return data;
}

struct listnode *stringsort(struct listnode *data)
{
		
	front_back* list=new front_back(); list->front = data; listnode* cursor;
	for (cursor=data; cursor!= NULL && cursor->next != NULL; cursor=cursor->next) {} list->back = cursor; //end of list
	list = ssort(list, 0);
	return list->front;
}

int main(void)
{  
   /*
    This is the Professor's test code. Scores were either pass 
    or fail depending if on the test code result and on the 
    time complexity of the program.
   */
   int i,j,k,l;
   struct listnode *node, *tmpnode; 
   node = NULL;
   for( i=0; i < 10; i++){
     for( j=0; j < 10; j++){
       for( k=0; k < 10; k++){
           tmpnode = node;
           node = (struct listnode *) malloc( sizeof(struct listnode));
           node->word = (char *) malloc( 50*sizeof(char));
           sprintf (node->word, "st %d %d %d",  (3*i)%10, (3*j)%10, (7*k)%10 ); 
           node->next = tmpnode;
       }
     }
   }
   tmpnode = node;
   node = (struct listnode *) malloc( sizeof(struct listnode));
   node->word = "first string";
   node->next = tmpnode;
   tmpnode = node;
   node = (struct listnode *) malloc( sizeof(struct listnode));
   node->word = "second string";
   node->next = tmpnode;
   tmpnode = node;
   node = (struct listnode *) malloc( sizeof(struct listnode));
   node->word = "the last string";
   node->next = tmpnode;
   printf("\n prepared list, now starting sort\n");
   node = stringsort(node);
   printf("\n checking sorted list\n");
   printf("1: %s\n", node->word);
   node = node->next;
   printf("2: %s\n", node->word);
   node=node->next;
   for( l=0; l < 1000; l++)
   {  if( node == NULL )
      {  printf("List ended early\n"); exit(0);
      }
      sscanf( node->word, "st %d %d %d", &i, &j, &k);
      if( 100*i + 10*j +k != l )
      {  printf("Node contains wrong value\n"); exit(0);
      }
      node = node->next;
   }
   printf("tested %d strings, found in sorted order.\n",l);
   printf("last: %s\n", node->word);
   if( node->next != NULL )
   {  printf("List too long\n"); exit(0);
   }
   exit(0);
}
