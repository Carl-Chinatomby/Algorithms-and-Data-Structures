/*
Implements a Bloom Filter for 200000 strings with an error rate of 1% 
using Universal Hash functions as described in 
Section 9.2 of Advanced Data Structures By Peter Brass
By Carl Chinatomby
Fall 2010

Assignment: 
Implement a Bloom filter for 200000 strings with an error rate of 1%.
To achieve this, you create ten bit arrays, each of 200000 bits (that is,
25000 char). For each of these, you select a has function h from a 
universal family. To insert a string s, you set the h[i](S-th) bit to
1 in the i-th bit array, for i=0..9. To query whether a string q is
contained in the set, you must check whether h[i](q) is one in the
i-th bit array for all i. 
This Structure must support the following operations:
 * bf_t *create_bf() Creates a bloom filter with above specifications.
 * void insert_bf(bf_t *b char *s) inserts the string *s into the 
   bloom filter *b.
 * int is_element(bf_t *b, char *q) returns 1 if the string *q is accepted
   by the bloom filter, and 0 else. 

Comments: Used a freelist for allocation/deallocation
*/

#include <iostream>
#include <cmath>
#include <stdlib.h>
#include <stdio.h>
#include <time.h>
using namespace std;

#define FILTERSIZE 25000 //bytes which equals 200000 bits
#define FILTERSIZEBITS FILTERSIZE*BITS
#define BITS 8
//#define MAXP 46337  /* prime, and 46337*46337 < 2147483647 */
#define MAXP 227832 /*Mersenne prime closest to 200000 */
#define TABLESIZE 10 //Number of arrays that we are keeping to guarantee the 1% - need 10 for 200000 size strings
#define BLOCKSIZE 256

//bit mask to reference the hext value for whata bit needs to be changed
//the least significant bit in a hex digit is the 1st bit(position) and the 
//most significant bit is the 8th bit(position)
unsigned char bit_mask[BITS] = {
	0x01,  //00000001
	0x02,  //00000010
	0x04,  //00000100
	0x08,  //00001000
	0x10,  //00010000 
	0x20,  //00100000
	0x40,  //01000000
	0x80   //10000000
};

typedef struct l_node {  char      *key;
char  *obj;
struct l_node  *next; } list_node_t;

typedef struct htp_l_node { int a; 
struct htp_l_node *next; } htp_l_node_t; 

typedef struct { int b;   int size; 
struct htp_l_node *a_list;} hf_param_t;

//outputs the bits of a char
void display_bits(unsigned char s){
	int value;
	for (int j=0; j<BITS; j++){
		value = s & (1 != 0);
		cout << value;
		s = s >> 1;
	}
}

typedef struct bloom_filter{
    unsigned char hashtables[TABLESIZE][FILTERSIZE];
	int (*hash_function)(char *, hf_param_t);
	hf_param_t hf_params[TABLESIZE];
} bf_t;

list_node_t *currentblock = NULL;
int    size_left;
list_node_t *free_list = NULL;

list_node_t *get_node(){ 
	list_node_t *tmp;
if( free_list != NULL ){ 
	tmp = free_list;
free_list = free_list -> next;
}
else{  
	if( currentblock == NULL || size_left == 0)
{  
	currentblock = (list_node_t *) malloc( BLOCKSIZE * sizeof(list_node_t) );
size_left = BLOCKSIZE;
}
tmp = currentblock++;
size_left -= 1;
}
return( tmp );
}

void return_node(list_node_t *node)
{  
	node->next = free_list;
free_list = node;
}

int universalhashfunction(char *key, hf_param_t hfp)
{  
	int sum;
	htp_l_node_t *al;
	sum = hfp.b;
	al = hfp.a_list;

	while( *key != '\0' ){  
		if( al->next == NULL ){   
			al->next = (htp_l_node_t *) get_node();
			al->next->next = NULL;
			al->a = rand()%MAXP;
		}
		sum += ( (abs((al->a)*((int) *key))))%MAXP;
		key += 1;
		al = al->next;
	}
	return( sum%hfp.size );
}

//creates a Bloom Filter with the above specification
bf_t *create_bf(){
	int i, j;
	bf_t *hash;
	srand ( (unsigned)time ( NULL ) );

	hash = (bf_t *) malloc( sizeof(bf_t) );

	//initializations
    for (i=0; i< TABLESIZE; i++){  
       for (j=0; j< FILTERSIZE; j++){
          (hash->hashtables)[i][j] = 0;
       }
	}
	hash->hash_function = universalhashfunction;

	//generate random values for all the parameters
	for (i=0; i< TABLESIZE; i++){
       hash->hf_params[i].b = rand()%MAXP;
       hash->hf_params[i].size = FILTERSIZEBITS;
       hash->hf_params[i].a_list = (htp_l_node_t *) get_node();
       hash->hf_params[i].a_list->next = NULL;
    }   
	return hash;
}


//inserts the string *s into the Bloom filter *b
void insert_bf(bf_t *b, char *s){
	int ind,i;
    for (i=0; i<TABLESIZE; i++){ 
       ind=b->hash_function(s, b->hf_params[i]);
       b->hashtables[i][(ind/BITS)] = b->hashtables[i][(ind/BITS)] | bit_mask[ind%BITS];
    }
}

//returns 1 if the string *q is accepted by the bloom filter, and 0 else. 
int is_element(bf_t *b, char *q){
	int result=0, i, ind;

    for (i=0; i< TABLESIZE; i++){
       ind = b->hash_function(q, b->hf_params[i]);
       result += ((b->hashtables[i][ind/BITS] & bit_mask[ind%BITS]) != 0x00);
    }
   return (result != TABLESIZE) ? 0 : 1;
}
/*
 Below is the Professor's test code. Scores were either pass
 or fail depending on the time complexity of the program and 
 outputting numbers close to 4000 (1% of 200,000 for false 
 postives) and also producing 0% False Negatives. 
*/


//Test Functions
void sample_string_A(char *s, int i)
{  s[0] = (char)(1 + (i%254));
s[1] = (char)(1 + ((i/254)%254));
s[2] = (char)(1 + (((i/254)/254)%254));
s[3] = 'a';
s[4] = 'b';
s[5] = (char)(1 + ((i*(i-3)) %217));
s[6] = (char)(1 + ((17*i+129)%233 ));
s[7] = '\0';
}
void sample_string_B(char *s, int i)
{  s[0] = (char)(1 + (i%254));
s[1] = (char)(1 + ((i/254)%254));
s[2] = (char)(1 + (((i/254)/254)%254));
s[3] = 'a';
s[4] = (char)(1 + ((i*(i-3)) %217));
s[5] = (char)(1 + ((17*i+129)%233 ));
s[6] = '\0';
}
void sample_string_C(char *s, int i)
{  s[0] = (char)(1 + (i%254));
s[1] = (char)(1 + ((i/254)%254));
s[2] = 'a';
s[3] = (char)(1 + ((i*(i-3)) %217));
s[4] = (char)(1 + ((17*i+129)%233 ));
s[5] = '\0';
}
void sample_string_D(char *s, int i)
{  s[0] = (char)(1 + (i%254));
s[1] = (char)(1 + ((i/254)%254));
s[2] = (char)(1 + (((i/254)/254)%254));
s[3] = 'b';
s[4] = 'b';
s[5] = (char)(1 + ((i*(i-3)) %217));
s[6] = (char)(1 + ((17*i+129)%233 ));
s[7] = '\0';
}
void sample_string_E(char *s, int i)
{  s[0] = (char)(1 + (i%254));
s[1] = (char)(1 + ((i/254)%254));
s[2] = (char)(1 + (((i/254)/254)%254));
s[3] = 'a';
s[4] = (char)(2 + ((i*(i-3)) %217));
s[5] = (char)(1 + ((17*i+129)%233 ));
s[6] = '\0';
}

int current_i = 0;

int main()
{  
	long i,j; 
bf_t * bloom;
bloom = create_bf();
printf("Created Filter\n");
for( i= 0; i< 100000; i++ )
{  char s[8];
sample_string_A(s,i);
insert_bf( bloom, s );
}
for( i= 0; i< 50000; i++ )
{  char s[7];
sample_string_B(s,i);
insert_bf( bloom, s );
}


for( i= 0; i< 50000; i++ )
{  char s[6];
sample_string_C(s,i);
insert_bf( bloom, s );
}


printf("inserted 200000 strings of length 8,7,6.\n");

for( i= 0; i< 100000; i++ )
{  char s[8];
sample_string_A(s,i);
if( is_element( bloom, s ) != 1 )
{  printf("found negative error (1)\n"); exit(0); }
}

for( i= 0; i< 50000; i++ )
{  char s[7];
sample_string_B(s,i);
if( is_element( bloom, s ) != 1 )
{  printf("found negative error (2)\n"); exit(0); }
}
for( i= 0; i< 50000; i++ )
{  char s[6];
sample_string_C(s,i);
if( is_element( bloom, s ) != 1 )
{  printf("found negative error (3)\n"); exit(0); }
}
j = 0;

for( i= 0; i< 200000; i++ )
{  char s[8];
sample_string_D(s,i);
if( is_element( bloom, s ) != 0 )
	j+=1;
}
for( i= 0; i< 200000; i++ )
{  char s[7];
sample_string_E(s,i); 
if( is_element( bloom, s ) != 0 )
	j+=1;
}

printf("Found %d positive errors out of 400000 tests.n",j);

} 


