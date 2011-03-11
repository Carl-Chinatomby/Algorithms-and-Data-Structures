/*
*********************
By Carl Chinatomby
*********************
Prof. Peter Brass
Adv. Data Structures
Fall 2010 Homework#1

Assignment:

Suppose you want ot keep track of a set of angular values; these are
float numbers in the range [0, 360[. You want to answer for any angular
interval, how many values are in that interval. But the query intervals 
can wrap around, e.g., [330, 30[ is a valid query interval. You also
want to give the first and last angle in the query interval, if it is
not empty. So your structure needs to support the following operations:
 * angle_set_t * create_aset() creates an empty angle set. 
 * void insert_aset(angle_set_t *s, float a) inserts the angle a into
   your set.
 * void delete_aset(angle_set_t *s, float a) deletes the angle a from 
   your set.
 * float first_aset(angle_set_t *s, float a, float b) returns the first
   angle in the interval [a, b[.
 * float last_aset(angle_set_t, *s, float a, float b) returns the last 
   angle in the interval [a, b[
 * int count_aset(angle_set_t *s, float a, float b) returns the number
   of angles in teh interval [a,b[
 
 You can use one of the search tress from my sample code at:
 http://www-cs.engr.ccny.cuny.edu/~peter/dstest.html
 as base implementation. Any implementation which needs to scan the 
 entire list of angle values to answer the queries is too slow and will
 be rejected. 
 
 Comments: I used the height balanced tree. The full sample code is
 supplied as a separate file. The leaf node method of trees was preferred.
*/ 
#include <stdio.h>
#include <stdlib.h>
using namespace std;

#define BLOCKSIZE 256

typedef struct tr_n_t { 
	float        key;
	struct tr_n_t  *left;
	struct tr_n_t *right;
	int           height; 
} angle_set_t;

angle_set_t *currentblock = NULL;
int    size_left;
angle_set_t *free_list = NULL;

//gets a node from the freelist if possible, otherwise allocates 
//a new node from heap
angle_set_t *get_node(){ 
	angle_set_t *tmp;
	if( free_list != NULL ){  
		tmp = free_list;
		free_list = free_list -> left;
	}
	else{ 
		if( currentblock == NULL || size_left == 0){  
			currentblock = (angle_set_t *) malloc( BLOCKSIZE * sizeof(angle_set_t) );
			size_left = BLOCKSIZE;
		}
		tmp = currentblock++;
		size_left -= 1;
	}
	return( tmp );
}

//return a note to the free list 
void return_node(angle_set_t *node){  
	node->left = free_list;
	free_list = node;
}

//creates an angle set with null values and an empty node
angle_set_t *create_aset(void){  
	angle_set_t *tmp_node;
	tmp_node = get_node();
	tmp_node->left = NULL;
	return( tmp_node );
}

//performs a left rotation on the tree
void left_rotation(angle_set_t *n){  
	angle_set_t *tmp_node;
	float        tmp_key;
	tmp_node = n->left; 
	tmp_key  = n->key;
	n->left  = n->right;        
	n->key   = n->right->key;
	n->right = n->left->right;  
	n->left->right = n->left->left;
	n->left->left  = tmp_node;
	n->left->key   = tmp_key;
}

//performs a right rotation on the tree
void right_rotation(angle_set_t *n){  
	angle_set_t *tmp_node;
	float        tmp_key;
	tmp_node = n->right; 
	tmp_key  = n->key;
	n->right = n->left;        
	n->key   = n->left->key;
	n->left  = n->right->left;  
	n->right->left = n->right->right;
	n->right->right  = tmp_node;
	n->right->key   = tmp_key;
}

//inserts an angle into the angleset *s with value new_key
void insert_aset(angle_set_t *s, float new_key){  
	angle_set_t *tmp_node;
	float* tmp_obj = (float*) malloc (sizeof(new_key));
	*tmp_obj = new_key;
	int finished;
	if( s->left == NULL ){   
		s->left = (angle_set_t*) &tmp_obj;
		s->key  = new_key;
		s->height = 0;
		s->right  = NULL; 
	}
	else{  
		angle_set_t * path_stack[100]; int  path_st_p = 0;
		tmp_node = s; 
		while( tmp_node->right != NULL ){   
			path_stack[path_st_p++] = tmp_node;
			if( new_key < tmp_node->key )
				tmp_node = tmp_node->left;
			else
				tmp_node = tmp_node->right;
		}
		/* found the candidate leaf. Test whether key distinct */
		if( tmp_node->key == new_key )
			return;
		/* key is distinct, now perform the insert_aset */ 
		{  
			angle_set_t *old_leaf, *new_leaf;
			old_leaf = get_node();
			old_leaf->left = tmp_node->left; 
			old_leaf->key = tmp_node->key;
			old_leaf->right  = NULL;
			old_leaf->height = 0;
			new_leaf = get_node();
			new_leaf->left = (angle_set_t*) &tmp_obj; 
			new_leaf->key = new_key;
			new_leaf->right  = NULL;
			new_leaf->height = 0; 
			if( tmp_node->key < new_key ){   
				tmp_node->left  = old_leaf;
				tmp_node->right = new_leaf;
				tmp_node->key = new_key;
			} 
			else{   
				tmp_node->left  = new_leaf;
				tmp_node->right = old_leaf;
			} 
			tmp_node->height = 1;
		}
		/* rebalance */
		finished = 0;
		while( path_st_p > 0 && !finished ){  
			int tmp_height, old_height;
			tmp_node = path_stack[--path_st_p];
			old_height= tmp_node->height;
			if( tmp_node->left->height - tmp_node->right->height == 2 ){  
				if( tmp_node->left->left->height - 
					tmp_node->right->height == 1 ){  
					right_rotation( tmp_node );
					tmp_node->right->height = 
						tmp_node->right->left->height + 1;
					tmp_node->height = tmp_node->right->height + 1;
				}
				else{  
					left_rotation( tmp_node->left );
					right_rotation( tmp_node );
					tmp_height = tmp_node->left->left->height; 
					tmp_node->left->height  = tmp_height + 1; 
					tmp_node->right->height = tmp_height + 1; 
					tmp_node->height = tmp_height + 2; 
				}
			}
			else if ( tmp_node->left->height - tmp_node->right->height == -2 ){  
				if( tmp_node->right->right->height - tmp_node->left->height == 1 ){  
					left_rotation( tmp_node );
					tmp_node->left->height = tmp_node->left->right->height + 1;
					tmp_node->height = tmp_node->left->height + 1;
				}
				else{  
					right_rotation( tmp_node->right );
					left_rotation( tmp_node );
					tmp_height = tmp_node->right->right->height; 
					tmp_node->left->height  = tmp_height + 1; 
					tmp_node->right->height = tmp_height + 1; 
					tmp_node->height = tmp_height + 2; 
				}
			}
			else /* update height even if there was no rotation */ {  
				if( tmp_node->left->height > tmp_node->right->height )
                    tmp_node->height = tmp_node->left->height + 1;
				else
					tmp_node->height = tmp_node->right->height + 1;
			}
			if( tmp_node->height == old_height )
				finished = 1;
		}

	}
	return;
}


//removes angle from the angle set *s
void delete_aset(angle_set_t *s, float delete_aset_key){  
	angle_set_t *tmp_node, *upper_node, *other_node;
	int finished;
	if( s->left == NULL )
		return;
	else if( s->right == NULL ){  
		if(  s->key == delete_aset_key ){  
			s->left = NULL;
			return;
		}
		else
			return;
	}
	else
	{  
		angle_set_t * path_stack[100]; int path_st_p = 0;
		tmp_node = s;
		while( tmp_node->right != NULL ){   
			path_stack[path_st_p++] = tmp_node;  
			upper_node = tmp_node;
			if( delete_aset_key < tmp_node->key ){  
				tmp_node   = upper_node->left; 
				other_node = upper_node->right;
			} 
			else{  
				tmp_node   = upper_node->right; 
				other_node = upper_node->left;
			} 
		}
		if( tmp_node->key == delete_aset_key ){  
			upper_node->key   = other_node->key;
			upper_node->left  = other_node->left;
			upper_node->right = other_node->right;
			upper_node->height = other_node->height;
			return_node( tmp_node );
			return_node( other_node );
		}
		/*start rebalance*/  
		finished = 0; path_st_p -= 1;
		while( path_st_p > 0 && !finished ){  
			int tmp_height, old_height;
			tmp_node = path_stack[--path_st_p];
			old_height= tmp_node->height;
			if( tmp_node->left->height - tmp_node->right->height == 2 ){  
				if( tmp_node->left->left->height - tmp_node->right->height == 1 ){  
					right_rotation( tmp_node ); 
					tmp_node->right->height = 
						tmp_node->right->left->height + 1;
					tmp_node->height = tmp_node->right->height + 1;
				}
				else{  
					left_rotation( tmp_node->left ); 
					right_rotation( tmp_node );
					tmp_height = tmp_node->left->left->height; 
					tmp_node->left->height  = tmp_height + 1; 
					tmp_node->right->height = tmp_height + 1; 
					tmp_node->height = tmp_height + 2; 
				}
			}
			else if ( tmp_node->left->height - tmp_node->right->height == -2 ){  
				if( tmp_node->right->right->height - tmp_node->left->height == 1 ){  
					left_rotation( tmp_node ); 
					tmp_node->left->height = 
						tmp_node->left->right->height + 1;
					tmp_node->height = tmp_node->left->height + 1;
				}
				else{  
					right_rotation( tmp_node->right );
					left_rotation( tmp_node );
					tmp_height = tmp_node->right->right->height; 
					tmp_node->left->height  = tmp_height + 1; 
					tmp_node->right->height = tmp_height + 1; 
					tmp_node->height = tmp_height + 2; 
				}
			}
			else /* update height even if there was no rotation */ 
			{  
				if( tmp_node->left->height > tmp_node->right->height )
					tmp_node->height = tmp_node->left->height + 1;
				else
					tmp_node->height = tmp_node->right->height + 1;
			}
			if( tmp_node->height == old_height )
				finished = 1;
		}
		/*end rebalance*/
		return;
	}
}

//returns the first angle in the angle set for the interval [a, b[. 
//Supports wrap around
float first_aset(angle_set_t *s, float a, float b){
	float max(360), min(0);
	bool wrap = false;
	float c;
	if (b - a < 0){
		wrap = true;
		c = b;
		b = max;
	}

	angle_set_t *tr_node;
	angle_set_t *node_stack[200]; int stack_p = 0;
	float result = -1;

	node_stack[stack_p++] = s;

	while( stack_p > 0 )
	{  
		tr_node = node_stack[--stack_p];
		if( tr_node->right == NULL ){  
           /* reached leaf, now test */
			if(a <= tr_node->key && tr_node->key < b ){  
				//if (result == -1)
				return result = tr_node->key;
				//else if (tr_node->key < result)
				//	result = tr_node->key;
			}
		} /* not leaf, might have to follow down */
		else if ( b <= tr_node->key ) /* entire interval left */
			node_stack[stack_p++] = tr_node->left;
		else if ( tr_node->key <= a ) /* entire interval right*/
			node_stack[stack_p++] = tr_node->right;
		else   /* node key in interval, follow left and right */{  
			node_stack[stack_p++] = tr_node->right;
			node_stack[stack_p++] = tr_node->left;
		}
	}
	//node was not found in [a,b[ for !wrap or [a, max[ for wrap, let's check [min, b[ for wrap
	a = min;
	node_stack[stack_p++] = s;
	if(result == -1){
		while( wrap && stack_p > 0  ){  
			tr_node = node_stack[--stack_p];
			if( tr_node->right == NULL ){  
               /* reached leaf, now test */
				if(a <= tr_node->key && tr_node->key < c ){  
					//if (result != -1 && tr_node->key < result)
					result = tr_node->key;
				}
			} /* not leaf, might have to follow down */
			else if ( c <= tr_node->key ) /* entire interval left */
				node_stack[stack_p++] = tr_node->left;
			else if ( tr_node->key <= a ) /* entire interval right*/
				node_stack[stack_p++] = tr_node->right;
			else   /* node key in interval, follow left and right */{  
				node_stack[stack_p++] = tr_node->left;
				node_stack[stack_p++] = tr_node->right;
			}
		}
	}
	return result;
}

//returns the last angle in the angle set for the interval [a, b[, 
//Supports wrap around
float last_aset(angle_set_t *s, float a, float b){
	float max(360), min(0);
	bool wrap = false;
	float c;
	if (b - a < 0){
		wrap = true;
		c = a;
		a = min;
	}

	angle_set_t *tr_node;
	angle_set_t *node_stack[200]; int stack_p = 0;
	float result = -1;

	node_stack[stack_p++] = s;

	while( stack_p > 0 ){  
		tr_node = node_stack[--stack_p];
		if( tr_node->right == NULL ){  
           /* reached leaf, now test */
			if(a <= tr_node->key && tr_node->key < b ){  
				return result = tr_node->key;
			}
		} /* not leaf, might have to follow down */
		else if ( b <= tr_node->key ) /* entire interval left */
			node_stack[stack_p++] = tr_node->left;
		else if ( tr_node->key <= a ) /* entire interval right*/
			node_stack[stack_p++] = tr_node->right;
		else   /* node key in interval, follow left and right */{  
			node_stack[stack_p++] = tr_node->left;
			node_stack[stack_p++] = tr_node->right;
		}
	}
	//node was not found in [a,b[ for !wrap or [a, max[ for wrap, let's check [min, b[ for wrap
	a = c;
	b = max;
	node_stack[stack_p++] = s;
	if(result == -1){
		while( wrap && stack_p > 0  ){  
			tr_node = node_stack[--stack_p];
			if( tr_node->right == NULL ){  
               /* reached leaf, now test */
				if(a <= tr_node->key && tr_node->key < c ){  
					result = tr_node->key;
				}
			} /* not leaf, might have to follow down */
			else if ( c <= tr_node->key ) /* entire interval left */
				node_stack[stack_p++] = tr_node->left;
			else if ( tr_node->key <= a ) /* entire interval right*/
				node_stack[stack_p++] = tr_node->right;
			else   /* node key in interval, follow left and right */
			{  
				node_stack[stack_p++] = tr_node->right;
				node_stack[stack_p++] = tr_node->left;
			}
		}
	}
	return result;
}

//returns the number of angles in the anglet that are between interval 
//[a, b[. Supports wrap around. 
int count_aset(angle_set_t *s, float a, float b){
	float max(360), min(0);
	int count = 0;
	bool wrap = false;
	float c;
	if (b - a < 0){
		wrap = true;
		c = b;
		b = max;
	}

	angle_set_t *tr_node;
	angle_set_t *node_stack[200]; int stack_p = 0;

	node_stack[stack_p++] = s;

	while( stack_p > 0 ){  
		tr_node = node_stack[--stack_p];
		if( tr_node->right == NULL ){  
           /* reached leaf, now test */
			if(a <= tr_node->key && tr_node->key < b ){  
				count++;
			}
		} /* not leaf, might have to follow down */
		else if ( b <= tr_node->key ) /* entire interval left */
			node_stack[stack_p++] = tr_node->left;
		else if ( tr_node->key <= a ) /* entire interval right*/
			node_stack[stack_p++] = tr_node->right;
		else   /* node key in interval, follow left and right */{  
			node_stack[stack_p++] = tr_node->right;
			node_stack[stack_p++] = tr_node->left;
		}
	}
	//node was not found in [a,b[ for !wrap or [a, max[ for wrap, let's check [min, b[ for wrap
	a = min;
	node_stack[stack_p++] = s;

	while( wrap && stack_p > 0  ){  
		tr_node = node_stack[--stack_p];
		if( tr_node->right == NULL ){  
           /* reached leaf, now test */
			if(a <= tr_node->key && tr_node->key < c ){  
				count++;
			}
		} /* not leaf, might have to follow down */
		else if ( c <= tr_node->key ) /* entire interval left */
			node_stack[stack_p++] = tr_node->left;
		else if ( tr_node->key <= a ) /* entire interval right*/
			node_stack[stack_p++] = tr_node->right;
		else   /* node key in interval, follow left and right */{  
			node_stack[stack_p++] = tr_node->left;
			node_stack[stack_p++] = tr_node->right;
		}
	}

	return count;
}


int main(void)
{ 
  /* 
   This is the Professor's test code Scores were either pass or fail
   depending on the time complexity of the program and having passing
   all the test code cases. There is a bug in this test code that causes
   the program to fail when results are correct due to comparison of floats
   9.90000 != to 9.9 in C. As long as the values matched, it should be a
   passing result. 
  */
   long i; float x, y;
  angle_set_t *S, *T;
  S = create_aset();
  T = create_aset();
  printf("Started: created two angle sets.\n");
  for( i= 0; i< 100000; i++ )
  { x = ( 3.0 * ((float) i)/ 1000.0 ) + 30.0;
    y = ( 3.0 * ( (float) ((81*i)%100000))/1000.0 ) + 30.0;
    insert_aset( S, x );
    insert_aset( T, y );
  }
  printf("Inserted same 100,000 angle values in both sets\n");
  x = first_aset(S, 0.0, 50.0);
  y = first_aset(T, 0.0, 50.0);
  if( x!=y)
    printf("Error: first angle in S is %f, in T is %f\n",x,y);
  x = last_aset(S, 320.0, 350.0);
  y = last_aset(T, 320.0, 350.0);
  if( x!=y)
    printf("Error: last angle in S is %f, in T is %f\n",x,y);
  
  for(i= 0; i<50; i++ )
  {  x = first_aset(S, 0.0, 100.0);
     delete_aset(S,x);
     y = first_aset(T, 0.0, 100.0);
     delete_aset(T,y);
     if( x!= y  )
       {  printf("Error in delete loop\n"); exit(-1); }
  }
  printf("Deleted first 50 elements\n");
  i = count_aset(S, 120.3, 175.6 );
  if( i != count_aset(T, 120.3, 175.6 ) )
    printf("Error in counting (1)\n");
  insert_aset(S, 11.7);   insert_aset(T, 11.7); 
  insert_aset(S, 13.0);   insert_aset(T, 13.0); 
  insert_aset(S, 9.9);   insert_aset(T, 9.9); 
  insert_aset(S, 355.0);   insert_aset(T, 355.0); 
  if( count_aset(S, 10.0, 20.0 ) != 2 || 
      count_aset(T, 10.0, 20.0 ) !=2 )
    printf("Error in counting (2)\n");
  if( count_aset(S, 350.0, 12.0 ) !=3 || 
      count_aset(T, 350.0, 12.0 ) !=3 )
    printf("Error in counting (3)\n");
  if( first_aset(S, 340.0, 20.0 ) != 355.0 || 
      first_aset(T, 340.0, 20.0 ) != 355.0 )
  {  printf("Error in wrap-around interval (1)\n");
     printf(" first in interval [340, 20) in S is %f, should be 355.0\n",
	 first_aset(S, 357.0, 20.0 ) );
     printf(" first in interval [340, 20) in T is %f, should be 355.0\n",
	 first_aset(T, 357.0, 20.0 ) );
  }
  if( last_aset(S, 340.0, 20.0 ) != 13.0 || 
      last_aset(T, 340.0, 20.0 ) != 13.0 )
  {  printf("Error in wrap-around interval (2)\n");
     printf(" last in interval [340, 20) in S is %f, should be 13.0\n",
	 first_aset(S, 357.0, 20.0 ) );
     printf(" last in interval [340, 20) in T is %f, should be 13.0\n",
	 first_aset(T, 357.0, 20.0 ) );
  }
  if( first_aset(S, 357.0, 20.0 ) != 9.9 || 
      first_aset(T, 357.0, 20.0 ) != 9.9 )
  {  printf("Error in wrap-around interval (3)\n");
     printf(" first in interval [357, 20) in S is %f, should be 9.9\n",
	 first_aset(S, 357.0, 20.0 ) );
     printf(" first in interval [357, 20) in T is %f, should be 9.9\n",
	 first_aset(T, 357.0, 20.0 ) );
  }
  if( last_aset(S, 357.0, 20.0 ) != 13.0 || 
      last_aset(T, 357.0, 20.0 ) != 13.0 )
  {  printf("Error in wrap-around interval (4)\n");
     printf(" last in interval [357, 20) in S is %f, should be 13.0\n",
	 last_aset(S, 357.0, 20.0 ) );
     printf(" last in interval [357, 20) in T is %f, should be 13.0\n",
	 last_aset(T, 357.0, 20.0 ) );
  }
  printf("End Test\n");
   exit(0);
}