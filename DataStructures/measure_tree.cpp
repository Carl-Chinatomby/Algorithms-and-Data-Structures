/*
The Measure Tree as Described in Section 4.3 of Advanced Data Structures By Peter Brass
By Carl Chinatomby
Fall 2010

Assignment: Implement the measure tree, as described in teh book chapter 4.3.
The measure tree is a dynamic structure that maintains a system of intervals
under insertion and deletion, and can answer the query: give the total length
of the union of the current intervals.

So the structure should support the following operations:
 * m_tree_t * create_m_tree() creates an empty measure tree
 * void insert_interval(m_tree_t *tree, int a, int b) inserts the 
   interval [a,b[.
 * void delete_interval(m_tree_t *tree, int a, int b) deletes the
   interval [a,b[. if it exists.
 * int query_length(m_tree *tree) returns the length of the union of
   all intervals in the current set.

Comments: Two freelists are used. The height balance search tree is also used.
All trees are implemented using the leaf method. The object of the first tree
is actually the root of another height balance search tree to keep track of the count. 
Duplicate measures are allowed and are tracked. When traversing the first tree,
each node represents an endpoint. the object of that node is the a tree that
denotes the opposite endpoint of that node interval. For instance inserting 
intervals (3, 6), (3, 5), (3, 7), (1, 3), (2, 3) would produce a tree with 
nodes [1, 2, 3, 5, 6, 7]. The objects of those leafs would each have a tree 
as follows:
 * 1 has tree [3]
 * 2 has tree [3]
 * 3 has tree [1, 2, 5, 6, 7]
 * 5 has tree [3]
 * 7 has tree [3]
 
*/

#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <algorithm>
using namespace std;

#define BLOCKSIZE 256
#define INF INT_MAX; //used as the upper bound for the right-most node in a tree

//measure tree structure
typedef struct m_t_t {
	int measure;
	int key;
	int height;
	m_t_t *left;
	m_t_t *right;
	int min; //this is l as described in the book
	int max; //this is r as described in the book
	int rightmax;
	int leftmin;
} m_tree_t;

//the tree to obtain the endpoints associated with each leaf in a measure tree
typedef struct interval_t_t {
	interval_t_t *left;
	interval_t_t *right;
	int key;
	int height;
	int count; 
} endpoint_tree;

//Measure Tree free_list initializations
m_tree_t *currentblock = NULL;
int    size_left;
m_tree_t *free_list = NULL;

//EndPoint Tree free_list initializations
endpoint_tree *currentendblock = NULL;
int    end_size_left;
endpoint_tree *endfree_list = NULL;

m_tree_t *get_node(){ 
	m_tree_t *tmp;
	if( free_list != NULL ){  
		tmp = free_list;
		free_list = free_list->left;
	}
	else{ 
		if( currentblock == NULL || size_left == 0){  
			currentblock = (m_tree_t *) malloc( BLOCKSIZE * sizeof(m_tree_t) );
			size_left = BLOCKSIZE;
		}
		tmp = currentblock++;
		size_left -= 1;
	}
	return( tmp );
}

void return_node(m_tree_t *node){  
	node->left = free_list;
	free_list = node;
}

endpoint_tree *get_end_node(){ 
	endpoint_tree *tmp;
	if( endfree_list != NULL ){  
		tmp = endfree_list;
		endfree_list = endfree_list->left;
	}
	else{ 
		if( currentendblock == NULL || end_size_left == 0){  
			currentendblock = (endpoint_tree *) malloc( BLOCKSIZE * sizeof(endpoint_tree) );
			end_size_left = BLOCKSIZE;
		}
		tmp = currentendblock++;
		end_size_left -= 1;
	}
	return( tmp );
}

void return_end_node(endpoint_tree *node){  
	node->left = endfree_list;
	endfree_list = node;
}


//pre: t is a correctly balanced leaf tree
//post: updates the measure for the the root of t.
void update_measure(m_tree_t *t){
	int l = t->min;
	int r = t->max;
	int rm = t->rightmax;
	if (t->right == NULL){
		if (r < rm)
			t->measure = r -l;
		else
			t->measure = rm - l;
	}
	else if ((t->right->leftmin < l) && (t->left->rightmax >= r))
		t->measure = r - l;
	else if ((t->right->leftmin >= l) && (t->left->rightmax >= r))
		t->measure = (r - t->key) + t->left->measure;
	else if ((t->right->leftmin < l) && (t->left->rightmax < r))
		t->measure = t->right->measure + (t->key - l);
	else //t->right->leftmin >= l && t=>left->rightmax < r
		t->measure = t->right->measure + t->left->measure;
}


//pre: t is a correctly balanced leaf tree
//post: updates the measure, min, max, leftmin, and right max if t has children, otherwise only updates the measure
void update_parameters(m_tree_t *t){
	if (t->right != NULL){
		t->min = t->left->min;
		t->max = t->right->max;
		t->leftmin = min(t->left->leftmin, t->right->leftmin);
		t->rightmax = max(t->left->rightmax, t->right->rightmax);
		update_measure(t);
	}
	else
		update_measure(t);
}



//left rotation for the endpoint tree within the measure tree
void endpoint_left_rotation(endpoint_tree *n){  
	endpoint_tree *tmp_node;
	int        tmp_key;
	tmp_node = n->left; 
	tmp_key  = n->key;
	n->left  = n->right;        
	n->key   = n->right->key;
	n->right = n->left->right;  
	n->left->right = n->left->left;
	n->left->left  = tmp_node;
	n->left->key   = tmp_key;
}

//right rotation for the endpoint tree within the measure tree
void endpoint_right_rotation(endpoint_tree *n){  
	endpoint_tree *tmp_node;
	int        tmp_key;
	tmp_node = n->right; 
	tmp_key  = n->key;
	n->right = n->left;        
	n->key   = n->left->key;
	n->left  = n->right->left;  
	n->right->left = n->right->right;
	n->right->right  = tmp_node;
	n->right->key   = tmp_key;
}


//pre: n is a leaf tree and not a leaf
//post: performs a left rotatation and calls update_paramters() on the affected nodes
void left_rotation(m_tree_t *n){  
   m_tree_t *tmp_node;
   int       tmp_key;
   tmp_node = n->left; 
   tmp_key  = n->key;
   n->left  = n->right;        
   n->key   = n->right->key;
   n->right = n->left->right;  
   n->left->right = n->left->left;
   n->left->left  = tmp_node;
   n->left->key   = tmp_key;
   update_parameters(n->left);
   update_parameters(n);
}

//pre: n is a leaf tree and not a leaf
//post: performs a right rotatation and calls update_paramters() on the affected nodes
void right_rotation(m_tree_t *n)
{  
   m_tree_t *tmp_node;
   int        tmp_key;
   tmp_node = n->right; 
   tmp_key  = n->key;
   n->right = n->left;        
   n->key   = n->left->key;
   n->left  = n->right->left;  
   n->right->left = n->right->right;
   n->right->right  = tmp_node;
   n->right->key   = tmp_key;
   update_parameters(n->right);
   update_parameters(n);
}


//verifies that t is not a leaf first and rebalances the tree 
void rebalance(m_tree_t* path_stack[], int path_st_p){
	int old_height, tmp_height;
	while (path_st_p > 0){
		m_tree_t* tmp_node = path_stack[--path_st_p];

		if (tmp_node->right != NULL){
			old_height=tmp_node->height;
			if( tmp_node->left->height - tmp_node->right->height == 2 ){  
				if( tmp_node->left->left->height - tmp_node->right->height == 1 ){  
					right_rotation( tmp_node );
			
				tmp_node->right->height = tmp_node->right->left->height + 1;
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
			else // update height even if there was no rotation  {  
				if( tmp_node->left->height > tmp_node->right->height ){
					tmp_node->height = tmp_node->left->height + 1;
					update_parameters(tmp_node);
				}
				else{
					tmp_node->height = tmp_node->right->height + 1;
					update_parameters(tmp_node);
				}
			}
		}
}
m_tree_t* create_m_tree(){
	m_tree_t* tree;
	tree = get_node();
	tree->key=INF;
	tree->min = tree->key;
	tree->max = tree->key;
	tree->leftmin = tree->key;
	tree->rightmax = tree->key;
	tree->height = 0;
	tree->right = NULL;
	tree->measure = 0;	
	return tree;
}

endpoint_tree* create_end_tree(){
	endpoint_tree* tree;
	tree = get_end_node();
	tree->left = NULL;
	return tree;
}

void insert_endpoint(endpoint_tree* s, int new_key){
	endpoint_tree *tmp_node;
	int* tmp_obj = (int*) malloc (sizeof(new_key));
	*tmp_obj = new_key;
	int finished;
	if( s->left == NULL ){  
		s->left = (endpoint_tree*) tmp_obj;
		s->key  = new_key;
		s->height = 0;
		s->right  = NULL; 
		s->count = 1;
	}
	else{  
		endpoint_tree * path_stack[100]; int  path_st_p = 0;
		tmp_node = s; 
		while( tmp_node->right != NULL ){   
			path_stack[path_st_p++] = tmp_node;
			if( new_key < tmp_node->key )
				tmp_node = tmp_node->left;
			else
				tmp_node = tmp_node->right;
		}
		/* found the candidate leaf. Test whether key distinct */
		if( tmp_node->key == new_key ){
			tmp_node->count++;
			return;
		} 
		else {	/* key is distinct, now perform the insert_aset */ 
			endpoint_tree *old_leaf, *new_leaf;
			old_leaf = get_end_node();
			old_leaf->left = tmp_node->left; 
			old_leaf->key = tmp_node->key;
			old_leaf->count = tmp_node->count;
			old_leaf->right  = NULL;
			old_leaf->height = 0;
			new_leaf = get_end_node();
			new_leaf->left = (endpoint_tree*) tmp_obj; 
			new_leaf->key = new_key;
			new_leaf->right  = NULL;
			new_leaf->height = 0; 
			new_leaf->count = 1;
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
				if( tmp_node->left->left->height - tmp_node->right->height == 1 ){  
					endpoint_right_rotation( tmp_node );
					tmp_node->right->height = tmp_node->right->left->height + 1;
					tmp_node->height = tmp_node->right->height + 1;
				}
				else{  
					endpoint_left_rotation( tmp_node->left );
					endpoint_right_rotation( tmp_node );
					tmp_height = tmp_node->left->left->height; 
					tmp_node->left->height  = tmp_height + 1; 
					tmp_node->right->height = tmp_height + 1; 
					tmp_node->height = tmp_height + 2; 
				}
			}
			else if ( tmp_node->left->height - tmp_node->right->height == -2 ){  
				if( tmp_node->right->right->height - tmp_node->left->height == 1 ){  
					endpoint_left_rotation( tmp_node );
					tmp_node->left->height = tmp_node->left->right->height + 1;
					tmp_node->height = tmp_node->left->height + 1;
				}
				else{  
					endpoint_right_rotation( tmp_node->right );
					endpoint_left_rotation( tmp_node );
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
	}
	return;
}

void delete_endpoint(endpoint_tree* s, int delete_key){
	endpoint_tree *tmp_node, *upper_node, *other_node;
	int finished;
	//Invalid Tree
	if( s->left == NULL )
		return;
	//Leaf
	else if( s->right == NULL )
	{  
		//verify if there are multiple occurances then decrement count or remove object
		if(  s->key == delete_key ){  
			if (s->count > 1)
				s->count--;
			else 
				s->left = NULL;

			return;
		}
		else
			return;
	}
	else{  
		endpoint_tree* path_stack[100]; int path_st_p = 0;
		tmp_node = s;
		while( tmp_node->right != NULL ){   
			path_stack[path_st_p++] = tmp_node;  
			upper_node = tmp_node;
			if( delete_key < tmp_node->key ){  
				tmp_node   = upper_node->left; 
				other_node = upper_node->right;
			} 
			else{  
				tmp_node   = upper_node->right; 
				other_node = upper_node->left;
			} 
		}
		if( tmp_node->key == delete_key && tmp_node->count > 1){
			tmp_node->count--;
			return;
		}
		else if( tmp_node->key == delete_key ){  
			upper_node->key   = other_node->key;
			upper_node->left  = other_node->left;
			upper_node->right = other_node->right;
			upper_node->height = other_node->height;
			return_end_node( tmp_node );
			return_end_node( other_node );
		}
		/*start rebalance*/  
		finished = 0; path_st_p -= 1;
		while( path_st_p > 0 && !finished ){  
			int tmp_height, old_height;
			tmp_node = path_stack[--path_st_p];
			old_height= tmp_node->height;
			if( tmp_node->left->height - tmp_node->right->height == 2 ){  
				if( tmp_node->left->left->height - tmp_node->right->height == 1 ){  
					endpoint_right_rotation( tmp_node ); 
					tmp_node->right->height = tmp_node->right->left->height + 1;
					tmp_node->height = tmp_node->right->height + 1;
				}
				else{  
					endpoint_left_rotation( tmp_node->left ); 
					endpoint_right_rotation( tmp_node );
					tmp_height = tmp_node->left->left->height; 
					tmp_node->left->height  = tmp_height + 1; 
					tmp_node->right->height = tmp_height + 1; 
					tmp_node->height = tmp_height + 2; 
				}
			}
			else if ( tmp_node->left->height - tmp_node->right->height == -2 ){  
				if( tmp_node->right->right->height - tmp_node->left->height == 1 ){  
					endpoint_left_rotation( tmp_node ); 
					tmp_node->left->height = tmp_node->left->right->height + 1;
					tmp_node->height = tmp_node->left->height + 1;
				}
				else{  
					endpoint_right_rotation( tmp_node->right );
					endpoint_left_rotation( tmp_node );
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
		/*end rebalance*/
		return;
	}
}

//pre: s is a correctly balanced endpoint tree
//post: returns the key of the largest value in s
int find_end_max(endpoint_tree* s){
	while (s->right != NULL){
		s=s->right;
	}
	return s->key;
}

//pre: s is a correctly balanced endpoint tree
//post: returns the key of the smallest value in s
int find_end_min(endpoint_tree* s){
	while (s->right != NULL){
		s=s->left;
	}
	return s->key;
}





//Inserts an interval in O(log n) time
void insert_interval(m_tree_t *tree, int a, int b){
	//empty tree - 
	if (tree->right == NULL) { 
		//build the single interval measure tree
		tree->key = b; 
		tree->right = get_node(); tree->right->key = b;																																					
		tree->left = get_node(); tree->left->key = a;

		//populate left child info
		tree->left->max = b; tree->left->min = a; 
		tree->left->rightmax = b; tree->left->leftmin = a;
		//create subtree for left child
		tree->left->right = NULL;
		tree->left->height = 0;
		endpoint_tree  *l = create_end_tree();	insert_endpoint(l, b);
		tree->left->left = (m_tree_t*) l;
		update_measure(tree->left);

		//populate right child info
		tree->right->max = INF;	tree->right->min = b;
		tree->right->rightmax = b;	tree->right->leftmin = a;
		//create subtree for right child
		tree->right->right = NULL;
		tree->right->height = 0;
		endpoint_tree *r = create_end_tree();	insert_endpoint(r, a);
		tree->right->left = (m_tree_t* ) r;
		update_measure(tree->right);

		//populate root
		//populate right child info
		tree->max = INF;	tree->min = a;
		tree->rightmax = b;	tree->leftmin = a;
		tree->height = 1;
		update_measure(tree);
	}
	else{
		m_tree_t *current_node, *right_path, *left_path, *lupdate_max, *rupdate_max;

		m_tree_t * path_stack[100]; int  path_st_p = 0;
		m_tree_t * left_path_stack[100]; int  lpath_st_p = 0;
		m_tree_t * right_path_stack[100]; int  rpath_st_p = 0;
		m_tree_t * update_max_stack[100]; int  max_st_p = 0;
		current_node = tree;
		right_path = left_path = lupdate_max = rupdate_max= NULL;
		endpoint_tree *l, *r;

		//search for a common ancestor
		while( current_node->right != NULL ) /* not at leaf */{   
			if( b < current_node->key ) {/* go left: a < b < key */
				path_stack[path_st_p++] = current_node;
				right_path = current_node->left;
				left_path  = current_node->left;
				current_node = current_node->left;
			}
			else if( current_node->key < a) {
				/* go right: key < b < a */
				path_stack[path_st_p++] = current_node;
				right_path = current_node->right;
				left_path  = current_node->right;    
				current_node = current_node->right;
			}
			else if( a < current_node->key && current_node->key < b )  /* split: a < key < b */ {   
				path_stack[path_st_p++] = current_node;
				right_path = current_node->right; /* both right */
				left_path  = current_node->left;    /* and left */
				break;
			}
			else if( a == current_node->key ) /* a = key < b */ {   
				//both must go right
				path_stack[path_st_p++] = current_node;
				right_path = current_node->right; /* no left */
				left_path = current_node->right;
				break;
			}
			else /*   current_node->key == b, so a < key = b */ {   
				path_stack[path_st_p++] = current_node;
				left_path  = current_node->left; /* no right */
				right_path = current_node->right;
				break;
			}
		}
		
		//travel the respective paths for the left and right endpoints
		if( left_path != NULL ) {  /* now follow the path of the left endpoint a*/
			while( left_path->right != NULL ){   
				if( a < left_path->key ) {   /* right node must be selected */
					left_path_stack[lpath_st_p++] = left_path;
					left_path = left_path->left;
				}
				else if ( a == left_path->key ){   
					lupdate_max=left_path->left;
					left_path_stack[lpath_st_p++] = left_path;
					left_path=left_path->right;
				}
				else {/* go right, no node selected */ 
					left_path_stack[lpath_st_p++] = left_path;
					left_path = left_path->right;
				}
			} 
			/* left leaf needs to be selected if reached in descent*/
			if( left_path->right == NULL && left_path->key == a ) {	//endpoint is already in path				
				//attach the end node and update all the parameters of nodes in path
				l = (endpoint_tree*) left_path->left;
				insert_endpoint(l, b);
				left_path->rightmax = find_end_max(l);
				left_path->left = (m_tree_t*) l;
				update_measure(left_path);
			}
			else { //no existing leaf, must create a new leaf
				left_path_stack[lpath_st_p++] = left_path;
				m_tree_t* rnode = get_node();	m_tree_t* lnode = get_node();
				if (a > left_path->key) { //b must now be the new root
					rnode->key = a;
					lnode->key = left_path->key;
					lnode->min = left_path->min;	lnode->max = left_path->max;
					lnode->rightmax = left_path->rightmax;	lnode->leftmin = left_path->leftmin;
					lnode->measure = left_path->measure;
					lnode->left = left_path->left;
					lnode->right = NULL;
					left_path->left = lnode;	left_path->right = rnode;
					left_path->key = a;
					left_path->left->height = 0;
					left_path->height = 1;
					l = create_end_tree();
					insert_endpoint(l, b);
					//ok so we are gonna update the leafs now, so that all other nodes can use the rules to update themselves
					left_path->right->left = (m_tree_t*) l; //store object
					left_path->right->right = NULL;
					left_path->right->height = 0;
					left_path->right->max = left_path->left->max;
					left_path->right->min = a; 
					left_path->right->leftmin = a;
					left_path->right->rightmax = b;
					left_path->left->max = a;
					update_measure(left_path->right);
					update_measure(left_path->left);
					//update the max of rightmost of the left tree
					if(lupdate_max != NULL){
						while (lupdate_max->right != NULL){
							update_max_stack[max_st_p++] = lupdate_max;
							lupdate_max = lupdate_max->right;
						}
						update_max_stack[max_st_p++] = lupdate_max;
						lupdate_max->max = left_path->key;

						while (max_st_p > 0){
							m_tree_t* upd = update_max_stack[--max_st_p];
							if (upd->right != NULL)
								update_parameters(upd);
							else
								update_measure(upd);
						}
					}
				}
				else { // strictly < than since we tested for equality earlier
					lnode->key = a;
					//m_tree_t* tmp = left_path;
					//left_path = rnode;	
					//left_path->right = tmp;
					rnode->key = left_path->key;
					rnode->min = left_path->min;	rnode->max = left_path->max;
					rnode->rightmax = left_path->rightmax;	rnode->leftmin = left_path->leftmin;
					rnode->measure = left_path->measure;
					rnode->left = left_path->left;
					rnode->right = NULL;
					left_path->left = lnode;	left_path->right = rnode;
					left_path->right->height = 0;
					left_path->height = 1;
					l = create_end_tree();
					insert_endpoint(l, b);
					left_path->left->left = (m_tree_t*) l; //store object
					left_path->left->right = NULL;
					left_path->left->height = 0;
					left_path->left->max = left_path->right->key;
					left_path->left->min = a; //
					left_path->left->leftmin = a;
					left_path->left->rightmax = b;	
					update_measure(left_path->left);
					update_measure(left_path->right);
					//update the max of rightmost of the left tree
					if(lupdate_max != NULL){
						while (lupdate_max->right != NULL){
							update_max_stack[max_st_p++] = lupdate_max;
							lupdate_max = lupdate_max->right;
						}
						update_max_stack[max_st_p++] = lupdate_max;
						lupdate_max->max = left_path->key;

						while (max_st_p > 0){
							m_tree_t* upd = update_max_stack[--max_st_p];
							if (upd->right != NULL)
								update_parameters(upd);
							else
								update_measure(upd);
						}
					}
				}	
			}
		}

		/* end left path */

		//SYMETTRICAL TO LEFT_PATH CASE
		if( right_path != NULL ){  /* and now follow the path of the right endpoint b */
			while( right_path->right != NULL ){   
				if( right_path->key < b ) {   /* left node must be selected */
					right_path_stack[rpath_st_p++] = right_path;
					right_path = right_path->right;
				}
				else if ( right_path->key == b){   
					rupdate_max=right_path->left;
					right_path_stack[rpath_st_p++] = right_path;
					right_path=right_path->right;
				}
				else /* go left, no node selected */ {
					right_path_stack[rpath_st_p++] = right_path;
					right_path = right_path->left;
				}
			}
			if( right_path->right == NULL && right_path->key == b ) {	//endpoint is already in path				
				//attach the end node and update all the parameters of nodes in path
				r = (endpoint_tree*) right_path->left;
				insert_endpoint(r, a);
				right_path->leftmin = find_end_min(r);
				update_measure(right_path);
			}
			else { //no existing leaf, must create a new leaf
				right_path_stack[rpath_st_p++] = right_path;
				m_tree_t* rnode = get_node();
				m_tree_t* lnode = get_node();
				if (b > right_path->key) { //b must now be the new root
					rnode->key = b;
					lnode->key = right_path->key;
					lnode->min = right_path->min;
					lnode->max = right_path->max;
					lnode->rightmax = right_path->rightmax;
					lnode->leftmin = right_path->leftmin;
					lnode->measure = right_path->measure;
					lnode->left = right_path->left;
					lnode->right = NULL;
					right_path->left = lnode;
					right_path->right = rnode;
					right_path->key = b;
					right_path->left->height = 0;
					right_path->height = 1;
					r = create_end_tree();
					insert_endpoint(r, a);
					//ok so we are gonna update the leafs now, so that all other nodes can use the rules to update themselves
					right_path->right->left = (m_tree_t*) r; //store object
					right_path->right->right = NULL;
					right_path->right->height = 0;
					right_path->right->max = right_path->left->max;
					right_path->right->min = b; 
					right_path->right->leftmin = a;
					right_path->right->rightmax = b;
					right_path->left->max = b;
					update_measure(right_path->right);
					update_measure(right_path->left);
					if(rupdate_max != NULL){
						while (rupdate_max->right != NULL){
							update_max_stack[max_st_p++]=rupdate_max;
							rupdate_max = rupdate_max->right;
						}
						update_max_stack[max_st_p++] = rupdate_max;
						rupdate_max->max = right_path->key;
						
						while (max_st_p > 0){
							m_tree_t* upd = update_max_stack[--max_st_p];
							if (upd->right != NULL)
								update_parameters(upd);
						}
					}
				}
				else { // strictly < than since we tested for equality earlier
					lnode->key = b;
					rnode->key = right_path->key;
					rnode->min = right_path->min;
					rnode->max = right_path->max;
					rnode->rightmax = right_path->rightmax;
					rnode->leftmin = right_path->leftmin;
					rnode->measure = right_path->measure;
					rnode->left = right_path->left;
					rnode->right = NULL;
					right_path->left = lnode;
					right_path->right = rnode;
					right_path->right->height = 0;
					right_path->height = 1;
					r = create_end_tree();
					insert_endpoint(r, a);
					right_path->left->left = (m_tree_t*) r; //store object
					right_path->left->right = NULL;
					right_path->left->height = 0;
					right_path->left->max = right_path->right->key;
					right_path->left->min = a; //
					right_path->left->leftmin = a;
					right_path->left->rightmax = b;
					update_measure(right_path->left);
					update_measure(right_path->right);
					if(rupdate_max != NULL){
						while (rupdate_max->right != NULL){
							update_max_stack[max_st_p++]=rupdate_max;
							rupdate_max = rupdate_max->right;
						}
						update_max_stack[max_st_p++] = rupdate_max;
						rupdate_max->max = right_path->key;
						
						while (max_st_p > 0){
							m_tree_t* upd = update_max_stack[--max_st_p];
							if (upd->right != NULL)
								update_parameters(upd);
						}
					}
				}
			}
		}  /* end right path */

		//ok leafs are inserted, now we need to rebalance and recalculate parameters
		rebalance(left_path_stack, lpath_st_p);
		rebalance(right_path_stack, rpath_st_p);
		rebalance(path_stack, path_st_p); //calulates the remainining nodes travelled before the split
	}
}

//deletes an interior node in O(log n) time (actually just changes the value to another node value)
void delete_interior_node(m_tree_t* tree, int a, int b){
	int last_key=tree->key;
	m_tree_t* tmp_node=tree->right;
	m_tree_t* tmp_path_stack[100]; int tmp_p = 0;
	if (tmp_node != NULL){
		while(tmp_node->right != NULL){
			tmp_path_stack[tmp_p++] = tmp_node;
			last_key = tmp_node->key;
			tmp_node=tmp_node->left;		
		}

		if (tmp_node->key != a && tmp_node->key != b){
			tree->key = tmp_node->key;
		}
		else if(last_key == b && (tmp_p > 0)) {
			tree->key = tmp_path_stack[--tmp_p]->key;
		}
		else {
			tree->key = last_key;
		}
	}
}


//deletes an inteval in O(log n) time 
void delete_interval(m_tree_t* tree, int a, int b){
	//interior node denotes an interior node that must be updated with a new value
	//the update_max variables denote a node where we must traverse go farthest right down its' left tree to update it's max
	m_tree_t *current_node, *right_path, *left_path, *lupdate_max, *rupdate_max, *interior;
	m_tree_t * path_stack[100]; int  path_st_p = 0;
	m_tree_t * left_path_stack[100]; int  lpath_st_p = 0;
	m_tree_t * right_path_stack[100]; int  rpath_st_p = 0;
	m_tree_t * update_max_stack[100]; int  max_st_p = 0;
	current_node = tree;
	right_path = left_path = lupdate_max = rupdate_max= interior = NULL;
	
	//search for a common ancestor then split
	while( current_node->right != NULL ) /* not at leaf */{   
		if( b < current_node->key ) {/* go left: a < b < key */
			path_stack[path_st_p++] = current_node;
			current_node = current_node->left;
		}
		else if( current_node->key < a) {
			/* go right: key < b < a */
			path_stack[path_st_p++] = current_node; 
			current_node = current_node->right;
		}
		else if( a < current_node->key && current_node->key < b )  /* split: a < key < b */ {   
			path_stack[path_st_p++] = current_node;
			right_path = current_node->right; /* both right */
			left_path  = current_node->left;    /* and left */
			break;
		}
		else if( a == current_node->key ) /* a = key < b */ {   
			//both must go right
			lupdate_max = current_node->left;
			right_path = current_node; 
			left_path = current_node;
			break;
		}
		else /*   current_node->key == b, so a < key = b */ { 
			//both must go right
			rupdate_max= current_node->left;
			left_path  = current_node; 
			right_path = current_node;
			break;
		}
	}

	//delete the larger value first (saves us from having to go back later on to update max)
	if( right_path != NULL ){  /* and now follow the path of the right endpoint b */
		while( right_path->right != NULL ){   
			if( right_path->key < b ) {   /* left node must be selected */
				right_path_stack[rpath_st_p++] = right_path;
				right_path = right_path->right;
			}
			else if ( right_path->key == b){   
				interior = right_path;
				rupdate_max=right_path->left;
				right_path_stack[rpath_st_p++] = right_path;
				right_path=right_path->right;
			}
			else /* go left, no node selected */ {
				right_path_stack[rpath_st_p++] = right_path;
				right_path = right_path->left;
			}
		}
		if( right_path->right == NULL && right_path->key == b ) 
		{
			endpoint_tree* et = (endpoint_tree*) right_path->left;
			delete_endpoint(et, a);
			if (et->left == NULL){ //empty endpoint tree, delete node
				return_end_node(et);
				delete_interior_node(interior, a, b);
				if (rpath_st_p > 0)
					right_path = right_path_stack[--rpath_st_p];
				else
					right_path = path_stack[--path_st_p];

				if (right_path->left->key == b){
					return_node(right_path->left);
					right_path->left = right_path->right->left;
					right_path->key = right_path->right->key;
					right_path->leftmin = right_path->right->leftmin;	right_path->rightmax = right_path->right->rightmax;
					right_path->min = right_path->right->min;	right_path->max = right_path->right->max;
					right_path->height = 0;
					m_tree_t* tmp = right_path->right;
					right_path->right = tmp->right;
					return_node(tmp);
					if (right_path->right != NULL) //update max for height+1 cases
						right_path->right->max = right_path->max;
					update_measure(right_path);
					//update the rightmost of the left tree to point to a new max and update measures/parameters
					if(rupdate_max != NULL){
						while (rupdate_max->right != NULL){
							update_max_stack[max_st_p++]=rupdate_max;
							rupdate_max = rupdate_max->right;
						}
						update_max_stack[max_st_p++]=rupdate_max;
						if (right_path->right != NULL)
							rupdate_max->max = right_path->left->key;
						else
							rupdate_max->max = right_path->key;

						while (max_st_p > 0){
							m_tree_t* upd = update_max_stack[--max_st_p];
							if (upd->right != NULL)
								update_parameters(upd);
							else
								update_measure(upd);
						}
					}
					if (left_path->right!= NULL)
						update_parameters(left_path);
				}
				else {			
					right_path->key = right_path->left->key;
					right_path->leftmin = right_path->left->leftmin;	right_path->rightmax = right_path->left->rightmax;
					right_path->min = right_path->left->min;	right_path->max = right_path->right->max;
					right_path->height = 0;
					return_node(right_path->right);
					m_tree_t* tmp = right_path->left;
					right_path->left = tmp->left;
					right_path->right = tmp->right;
					return_node(tmp);
					if (right_path->right != NULL){//update max for height+1 cases
						right_path->right->max = right_path->max;
						update_measure(right_path->right);
					}
					update_measure(right_path);
					//update the rightmost of the left tree to point to a new max and update measures/parameters
					if(rupdate_max != NULL){
						while (rupdate_max->right != NULL){
							update_max_stack[max_st_p++]=rupdate_max;
							rupdate_max = rupdate_max->right;
						}
						update_max_stack[max_st_p++] = rupdate_max;
						rupdate_max->max = right_path->max;

						while (max_st_p > 0){
							m_tree_t* upd = update_max_stack[--max_st_p];
							if (upd->right != NULL)
								update_parameters(upd);
							else
								update_measure(upd);
						}
					}
					if (right_path->right!= NULL)
						update_parameters(left_path);
				}
			}
			else{
				right_path->rightmax = max(right_path->key, find_end_max(et));
				right_path->leftmin = min(right_path->key, find_end_min(et));
				update_measure(right_path);
			}
		}
	}  /* end right path */

	max_st_p = 0;	interior = NULL;

	//SYMMETRICAL TO RIGHT_PATH CASE
	if( left_path != NULL ) {  /* now follow the path of the left endpoint a*/
		while( left_path->right != NULL )	{   
			if( a < left_path->key ) {   /* right node must be selected */
				left_path_stack[lpath_st_p++] = left_path;
				left_path = left_path->left;
			}
			else if ( a == left_path->key ){   
				lupdate_max=left_path->left;
				left_path_stack[lpath_st_p++] = left_path;
				interior=left_path;
				left_path=left_path->right;
			}
			else {/* go right, no node selected */ 
				left_path_stack[lpath_st_p++] = left_path;
				left_path = left_path->right;
			}
		} 
		/* left leaf needs to be selected if reached in descent*/
		if( left_path->right == NULL && left_path->key == a ) {	//at the left node to delete
			endpoint_tree* et = (endpoint_tree*) left_path->left;
			delete_endpoint(et, b);
			if (et->left == NULL){ //empty endpoint tree, delete node
				return_end_node(et);
				if (interior != NULL)
					delete_interior_node(interior, a, b);
				if (lpath_st_p > 0)
					left_path = left_path_stack[--lpath_st_p];
				else
					left_path = path_stack[--path_st_p];

				if (left_path->left->key == a){
					return_node(left_path->left);
					left_path->left = left_path->right->left;
					left_path->key = left_path->right->key;
					left_path->leftmin = left_path->right->leftmin;
					left_path->rightmax = left_path->right->rightmax;
					left_path->min = left_path->right->min;
					left_path->max = left_path->right->max;
					left_path->height = 0;
					m_tree_t* tmp = left_path->right;
					left_path->right = tmp->right;
					return_node(tmp);
					if (left_path->right != NULL)
						left_path->right->max = left_path->max;
					update_measure(left_path);
					if (lupdate_max != NULL){
						while (lupdate_max->right != NULL){
							update_max_stack[max_st_p++] = lupdate_max;
							lupdate_max = lupdate_max->right;
						}
						update_max_stack[max_st_p++] = lupdate_max;
						if (left_path->right != NULL)
							lupdate_max->max = left_path->left->key;
						else
							lupdate_max->max = left_path->key;
						
						while (max_st_p > 0){
							m_tree_t* upd = update_max_stack[--max_st_p];
							if (upd->right != NULL)
								update_parameters(upd);
							else
								update_measure(upd);
						}
					}
					if (left_path->right!= NULL)
						update_parameters(left_path);
				}
				else {			
					left_path->key = left_path->left->key;
					left_path->leftmin = left_path->left->leftmin;
					left_path->rightmax = left_path->left->rightmax;
					left_path->min = left_path->left->min;
					left_path->max = left_path->right->max;
					left_path->height = 0;
					return_node(left_path->right);
					m_tree_t* tmp = left_path->left;
					left_path->left = tmp->left;
					left_path->right = tmp->right;
					return_node(tmp);
					if (left_path->right != NULL){
						left_path->right->max = left_path->max;
						update_measure(left_path->left);
					}
					update_measure(left_path);
					if (lupdate_max != NULL){
						while (lupdate_max->right != NULL){
							update_max_stack[max_st_p++] = lupdate_max;
							lupdate_max = lupdate_max->right;
						}
						update_max_stack[max_st_p++] = lupdate_max; 
						lupdate_max->max = left_path->max;
						while (max_st_p > 0){
							m_tree_t* upd = update_max_stack[--max_st_p];
							if (upd->right != NULL)
								update_parameters(upd);
							else
								update_measure(upd);
						}
					}
					if (left_path->right!= NULL)
						update_parameters(left_path);	
				}
			}
			else{
				left_path->rightmax = max(left_path->key, find_end_max(et));
				left_path->leftmin = min(left_path->key, find_end_min(et));
				update_measure(left_path);
			}
		}

	}

	/* end left path */
	//ok leafs are deleted, now we need to rebalance and recalculate parameters
	rebalance(left_path_stack, lpath_st_p);
	rebalance(right_path_stack, rpath_st_p);
	rebalance(path_stack, path_st_p);
}

//returnes the measure in O(1) time
int query_length(m_tree_t *tree){
	return tree->measure;
}

int main(){
   /*
    This is the professor's test code. Scores were either pass 
    or fail depending on the time complexity of the program and
    succession of the test code. 
   */
	int i; m_tree_t *t; ;
   printf("starting \n");
   t = create_m_tree();
   for(i=0; i< 50; i++ )
      insert_interval( t, 2*i, 2*i +1 );
   printf("inserted first 50 intervals, total length is %d, should be 50.\n", query_length(t));
      insert_interval( t, 0, 100 );
   printf("inserted another interval, total length is %d, should be 100.\n", query_length(t));
   for(i=1; i< 50; i++ )
     insert_interval( t, 199 - (3*i), 200 ); /*[52,200] is longest*/
   printf("inserted further 49 intervals, total length is %d, should be 200.\n", query_length(t));
   for(i=2; i< 50; i++ )
     delete_interval(t, 2*i, 2*i +1 );
   delete_interval(t,0,100);
   printf("deleted some intervals, total length is %d, should be 150.\n", query_length(t));
   insert_interval( t, 1,2 ); 
   for(i=49; i>0; i-- )
     delete_interval( t, 199 - (3*i), 200 ); 
   insert_interval( t, 0,2 );
   insert_interval( t, 1,5 );  
   printf("deleted some intervals, total length is %d, should be 5.\n", query_length(t));
   insert_interval( t, 0, 100 );
   printf("inserted another interval, total length is %d, should be 100.\n", query_length(t));
   for(i=0; i<=3000; i++ )
      insert_interval( t, 2000+i, 3000+i ); 
   printf("inserted 3000 intervals, total length is %d, should be 4100.\n", query_length(t));
   for(i=0; i<=3000; i++ )
     delete_interval( t, 2000+i, 3000+i ); 
   printf("deleted 3000 intervals, total length is %d, should be 100.\n", query_length(t));
   for(i=0; i<=100; i++ )
      insert_interval( t, 10*i, 10*i+100 ); 
   printf("inserted another 100 intervals, total length is %d, should be 1100.\n", query_length(t));
   delete_interval( t, 1,2 ); 
   delete_interval( t, 0,2 ); 
   delete_interval( t, 2,3 ); 
   delete_interval( t, 0,1 ); 
   delete_interval( t, 1,5 );
   printf("deleted some intervals, total length is %d, should be still 1100.\n", query_length(t)); 
   for(i=0; i<= 100; i++ )
     delete_interval(t, 10*i, 10*i+100);
   delete_interval(t,0,100);
   printf("deleted last interval, total length is %d, should be 0.\n", query_length(t));

	return 0;
} 