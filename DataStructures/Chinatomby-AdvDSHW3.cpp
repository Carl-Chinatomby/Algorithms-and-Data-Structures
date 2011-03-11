/*
//The Linear Order Tree as Described in Section 6.5 of Advanced Data Structures By Peter Brass
//This implementation is not the same as described in the book and is slightly slower
By Carl Chinatomby
Fall 2010
*/
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef long key_t; //THIS LINE NEEDS TO BE COMMENTED OUT FOR G++ ON UBUNTU 10.04

#define BLOCKSIZE 256
#define INF LONG_MAX;
//linear order tree declaration
typedef struct linear_t {
	key_t key;
	linear_t *left;
	linear_t *right;
	linear_t *parent;
	//points to top and bottom for the root
	linear_t *top;
	linear_t *bottom;
	int height; 
} l_o_t; //linear order tree

//binary tree declaration
typedef struct list_t {
	key_t key;
	list_t *left;
	list_t *right;
	int height;
	l_o_t *l_o_tptr; //pointer to the root of the object tree (linear order tree) (only used on root of binary tree)
} o_t; //order tree (binary tree)

//linear order tree freelist initializations
l_o_t *currentblock = NULL;
int    size_left;
l_o_t *free_list = NULL;

//order tree initializations
o_t *currentotblock = NULL;
int    ot_size_left;
o_t *otfree_list = NULL;

//linear order tree freelist functions
l_o_t *get_node()
{ 
	l_o_t *tmp;
	if( free_list != NULL )
	{  
		tmp = free_list;
		free_list = free_list->left;
	}
	else
	{ 
		if( currentblock == NULL || size_left == 0)
		{  
			currentblock = 
				(l_o_t *) malloc( BLOCKSIZE * sizeof(l_o_t) );
			size_left = BLOCKSIZE;
		}
		tmp = currentblock++;
		size_left -= 1;
	}
	return( tmp );
}

void return_node(l_o_t *node)
{  
	node->left = free_list;
	free_list = node;
}

//order tree freelist functions
o_t *get_ot_node()
{ 
	o_t *tmp;
	if( otfree_list != NULL )
	{  
		tmp = otfree_list;
		otfree_list = otfree_list->left;
	}
	else
	{ 
		if( currentotblock == NULL || ot_size_left == 0)
		{  
			currentotblock = 
				(o_t *) malloc( BLOCKSIZE * sizeof(o_t) );
			ot_size_left = BLOCKSIZE;
		}
		tmp = currentotblock++;
		ot_size_left -= 1;
	}
	return( tmp );
}

void return_ot_node(o_t *node){  
	node->left = otfree_list;
	otfree_list = node;
}


//left rotation for the linear order tree linked by binary tree
void lot_left_rotation(l_o_t *n){  
	l_o_t *tmp_node;
	key_t        tmp_key;
	tmp_node = n->left; 
	tmp_key  = n->key;
	n->left  = n->right; //no need to update to parent
	n->key   = n->right->key;
	n->right = n->left->right;  
	n->right->parent = n;
	n->left->right = n->left->left;
	n->left->left  = tmp_node;
	n->left->left->parent = n->left;
	n->left->key   = tmp_key;
}

//right rotation for the linear order tree linked by binary tree
void lot_right_rotation(l_o_t *n){  
	l_o_t *tmp_node;
	key_t        tmp_key;
	tmp_node = n->right; 
	tmp_key  = n->key;
	n->right = n->left;        
	n->key   = n->left->key;
	n->left  = n->right->left;  
	n->left->parent = n;
	n->right->left = n->right->right;
	n->right->right  = tmp_node;
	n->right->right->parent= n->right;
	n->right->key   = tmp_key;
}

//pre: n is a leaf tree and not a leaf
//post: performs a left rotatation and calls update_paramters() on the affected nodes
void left_rotation(o_t *n){  
	o_t *tmp_node;
	key_t       tmp_key;
	tmp_node = n->left; 
	tmp_key  = n->key;
	n->left  = n->right;        
	n->key   = n->right->key;
	n->right = n->left->right;  
	n->left->right = n->left->left;
	n->left->left  = tmp_node;
	n->left->key   = tmp_key;
}

//performs a right rotation on the the order tree (binary tree)
void right_rotation(o_t *n){  
	o_t *tmp_node;
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

l_o_t* create_linear_order(){
	l_o_t* tree;
	tree = get_node();
	tree->key = (key_t) INF; //value doesn't matter, i use pointers to test for emptiness
	tree->parent = NULL;
	tree->left = NULL;
	tree->right = NULL;
	tree->top = tree; 
	tree->bottom = tree;
	tree->height = 0;
	return tree;
}

o_t* create_order(){
	o_t* tree = get_ot_node();
	l_o_t* lot_ptr = create_linear_order();
	tree->key = (key_t) INF; //value doesn't matter, i use pointers to test for emptiness
	tree->left = NULL;
	tree->right = NULL;
	tree->l_o_tptr = lot_ptr;
	tree->height = 0;
	return tree;
}

void rebalance(o_t* path_stack[], int path_st_p){
	o_t *tmp_node;
	int finished = 0;
	while( path_st_p > 0 && !finished )
	{  
		int tmp_height, old_height;
		tmp_node = path_stack[--path_st_p];
		old_height= tmp_node->height;
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
		else if ( tmp_node->left->height - tmp_node->right->height == -2 )
		{  
			if( tmp_node->right->right->height - tmp_node->left->height == 1 ){  
				left_rotation( tmp_node );
			tmp_node->left->height = tmp_node->left->right->height + 1;
			tmp_node->height = tmp_node->left->height + 1;
			}
			else
			{  
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
}

//inserts top or bottom on o_t tree (binary tree)
void o_t_insert(o_t* ord, key_t new_key, l_o_t* leaf){
	o_t *tmp_node;
	o_t *path_stack[100]; int  path_st_p = 0;
	tmp_node = ord; 
	while( tmp_node->right != NULL )
	{   
		path_stack[path_st_p++] = tmp_node;
		if( new_key < tmp_node->key )
			tmp_node = tmp_node->left;
		else
			tmp_node = tmp_node->right;
	}
	// found the candidate leaf. Test whether key distinct 
	if( tmp_node->key == new_key ){
		tmp_node->left = (o_t*) leaf;
		return;
	}
	// key is distinct, now perform the insert  
	{  
		o_t *old_leaf, *new_leaf;
		old_leaf = get_ot_node();
		old_leaf->left = tmp_node->left; 
		old_leaf->key = tmp_node->key;
		old_leaf->right  = NULL;
		old_leaf->l_o_tptr = NULL;
		old_leaf->height = 0;
		new_leaf = get_ot_node();
		new_leaf->left = (o_t*) leaf; 
		new_leaf->key = new_key;
		new_leaf->right  = NULL;
		new_leaf->l_o_tptr = NULL;
		new_leaf->height = 0; 
		if( tmp_node->key < new_key )
		{   
			tmp_node->left  = old_leaf;
			tmp_node->right = new_leaf;
			tmp_node->key = new_key;
		} 
		else
		{   
			tmp_node->left  = new_leaf;
			tmp_node->right = old_leaf;
		} 
		tmp_node->height = 1;
	}

	rebalance(path_stack, path_st_p);
}

void l_o_t_rebalance(l_o_t* tree){
	int finished = 0;
	l_o_t* tmp_node = tree;
	while( tmp_node->parent != NULL && !finished)
	{  
		int tmp_height, old_height;
		tmp_node = tmp_node->parent;
		old_height= tmp_node->height;
		if( tmp_node->left->height - tmp_node->right->height == 2 )
		{  
			if( tmp_node->left->left->height - tmp_node->right->height == 1 )
			{  
				lot_right_rotation( tmp_node );
				tmp_node->right->height = tmp_node->right->left->height + 1;
				tmp_node->height = tmp_node->right->height + 1;
			}
			else
			{  
				lot_left_rotation( tmp_node->left );
				lot_right_rotation( tmp_node );
				tmp_height = tmp_node->left->left->height; 
				tmp_node->left->height  = tmp_height + 1; 
				tmp_node->right->height = tmp_height + 1; 
				tmp_node->height = tmp_height + 2; 
			}
		}
		else if ( tmp_node->left->height -  tmp_node->right->height == -2 )
		{  
			if( tmp_node->right->right->height -  tmp_node->left->height == 1 )
			{  
				lot_left_rotation( tmp_node );
				tmp_node->left->height =  tmp_node->left->right->height + 1;
				tmp_node->height = tmp_node->left->height + 1;
			}
			else
			{ 
				lot_right_rotation( tmp_node->right );
				lot_left_rotation( tmp_node );
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

//inserts as smallest element (leftmost in linear order tree)
void insert_bottom(o_t *ord, key_t a){
	//empty tree
	if (ord->left == NULL){
		ord->key = a;
		ord->left = (o_t*) ord->l_o_tptr;
		ord->l_o_tptr->key = a;	
		return;
	}

	//tree has at least one item;
	//linear order insert
	o_t* current_node;
	l_o_t* newbottom = get_node();
	l_o_t* oldbottom = get_node();

	newbottom->key = a; newbottom->left = NULL; newbottom->right = NULL; 
	newbottom->top = NULL; newbottom->bottom = NULL; //only root will have these initalized, we dont really care for all the others
	newbottom->height = 0;

	oldbottom->key = ord->l_o_tptr->bottom->key; oldbottom->left = NULL; oldbottom->right = NULL;
	oldbottom->top=NULL; oldbottom->bottom = NULL; //only root will have these initialized, we dont really care for all the others
	oldbottom->height = 0;

	ord->l_o_tptr->bottom->left = newbottom;
	ord->l_o_tptr->bottom->right = oldbottom;
	newbottom->parent = ord->l_o_tptr->bottom;
	oldbottom->parent = ord->l_o_tptr->bottom;
	if(ord->l_o_tptr->bottom == ord->l_o_tptr->top){//check if tree was a single node before, if so the top needs to be updated
		ord->l_o_tptr->top = oldbottom;
	}
	ord->l_o_tptr->bottom = newbottom;

	//update pointer for o_t (binary tree) object of that leaf
	current_node = ord; 
	while( current_node->right != NULL ){   
		if( oldbottom->key < current_node->key )
			current_node = current_node->left;
		else
			current_node = current_node->right;
	}
	current_node->left = (o_t*) oldbottom;

	l_o_t_rebalance(newbottom);
	o_t_insert(ord, a, ord->l_o_tptr->bottom); //inserts into binary tree and rebalance
}



//inserts as largest element (rightmost in linear order tree)
void insert_top(o_t *ord, key_t a){
	//empty tree
	if (ord->left == NULL){
		ord->key = a;
		ord->left = (o_t*) ord->l_o_tptr;
		ord->l_o_tptr->key = a;
		return;
	}

	//tree has at least one item;
	//linear order insert
	o_t* current_node;
	l_o_t* newtop = get_node();
	l_o_t* oldtop = get_node();

	newtop->key = a; newtop->left = NULL; newtop->right = NULL; 
	newtop->top = NULL; newtop->bottom = NULL; //only root will have these initalized, we dont really care for all the others
	newtop->height = 0;

	oldtop->key = ord->l_o_tptr->top->key; oldtop->left = NULL; oldtop->right = NULL;
	oldtop->top=NULL; oldtop->bottom = NULL; //only root will have these initialized, we dont really care for all the others
	oldtop->height = 0;

	ord->l_o_tptr->top->right = newtop;
	ord->l_o_tptr->top->left = oldtop;
	newtop->parent = ord->l_o_tptr->top;
	oldtop->parent = ord->l_o_tptr->top;
	if(ord->l_o_tptr->bottom == ord->l_o_tptr->top){//check if tree was a single node before, if so the bottom needs to be updated
		ord->l_o_tptr->bottom = oldtop;
	}
	ord->l_o_tptr->top = newtop;

	//update pointer for o_t (binary tree) object of that leaf
	current_node = ord; 
	while( current_node->right != NULL ){   
		if( oldtop->key < current_node->key )
			current_node = current_node->left;
		else
			current_node = current_node->right;
	}
	current_node->left = (o_t*) oldtop;


	//linear order rebalance
	l_o_t_rebalance(newtop);
	o_t_insert(ord, a, ord->l_o_tptr->top); //inserts into binary tree and rebalance
}

void insert_before(o_t *ord, key_t a, key_t b){
	//find b in o_t tree
	o_t *current_node;
	current_node = ord; 
	while( current_node->right != NULL ){   
		if( b < current_node->key )
			current_node = current_node->left;
		else
			current_node = current_node->right;
	}
	//found leaf let's insert the new node in l_o_t tree;
	l_o_t* candleaf = (l_o_t*) current_node->left;
	l_o_t* newnode = get_node();
	l_o_t* oldnode = get_node();

	newnode->key = a; newnode->left = NULL; newnode->right = NULL; 
	newnode->top = NULL; newnode->bottom = NULL; //only root will have these initalized, we dont really care for all the others
	newnode->height = 0;

	oldnode->key = b; oldnode->left = NULL; oldnode->right = NULL;
	oldnode->top=NULL; oldnode->bottom = NULL; //only root will have these initialized, we dont really care for all the others
	oldnode->height = 0;

	candleaf->left = newnode;
	candleaf->right = oldnode;
	newnode->parent = candleaf;
	oldnode->parent = candleaf;
	//candleaf->height = 1;
	//verify if there were top or bottom and update those pointers
	if(ord->l_o_tptr->bottom == candleaf){
		ord->l_o_tptr->bottom = newnode;
	}

	if(ord->l_o_tptr->top == candleaf){
		ord->l_o_tptr->top = oldnode;
	}

	//update pointer for o_t (binary tree) object for b
	current_node->left = (o_t*) oldnode;
	
	//insert a into o_t (binary tree) and update it's pointer
	o_t_insert(ord, a, newnode);
	l_o_t_rebalance(newnode);

}

void insert_after(o_t *ord, key_t a, key_t b){
	//find b in o_t tree
	o_t *current_node;
	current_node = ord; 
	while( current_node->right != NULL ){   
		if( b < current_node->key )
			current_node = current_node->left;
		else
			current_node = current_node->right;
	}
	//found leaf let's insert the new node in l_o_t tree;
	l_o_t* candleaf = (l_o_t*) current_node->left;
	l_o_t* newnode = get_node();
	l_o_t* oldnode = get_node();

	newnode->key = a; newnode->left = NULL; newnode->right = NULL; 
	newnode->top = NULL; newnode->bottom = NULL; //only root will have these initalized, we dont really care for all the others
	newnode->height = 0;

	oldnode->key = b; oldnode->left = NULL; oldnode->right = NULL;
	oldnode->top=NULL; oldnode->bottom = NULL; //only root will have these initialized, we dont really care for all the others
	oldnode->height = 0;

	candleaf->right = newnode;
	candleaf->left = oldnode;
	newnode->parent = candleaf;
	oldnode->parent = candleaf;
	//candleaf->height = 1;
	//verify if there were top or bottom and update those pointers
	if(ord->l_o_tptr->bottom == candleaf){
		ord->l_o_tptr->bottom = oldnode;
	}

	if(ord->l_o_tptr->top == candleaf){
		ord->l_o_tptr->top = newnode;
	}

	//update pointer for o_t (binary tree) object for b
	current_node->left = (o_t*) oldnode;
	
	//insert a into o_t (binary tree) and update it's pointer
	o_t_insert(ord, a, newnode);
	l_o_t_rebalance(newnode);
}

void delete_o(o_t *ord, key_t a){
	//one item tree
	if (ord->right == NULL){
		ord->key = (key_t) INF;
		ord->left = NULL;
		ord->l_o_tptr->key = (key_t) INF;
	}
	//tree has at least one item
	//find a
	o_t *current_node, *previous, *tmp_node;
	o_t *path_stack[100]; int  path_st_p = 0;
	l_o_t *tmp_ptr = NULL;
	previous = tmp_node = NULL;
	current_node = ord; 
	while( current_node->right != NULL ){ 
		previous = current_node;
		path_stack[path_st_p++] = previous;
		if( a < current_node->key ){
			current_node = current_node->left;
		}
		else{
			current_node = current_node->right;
		}
	}
	//found leaf
	l_o_t* candleaf = (l_o_t*) current_node->left;
	//update pointers if this was top or bottom
	if (ord->l_o_tptr->top->parent == candleaf->parent){
		ord->l_o_tptr->top = candleaf->parent;

	}
	if (ord->l_o_tptr->bottom->parent == candleaf->parent ){
		ord->l_o_tptr->bottom = candleaf->parent;
	}

	//delete node from linear order tree
	if (candleaf->parent->right == candleaf){
		candleaf=candleaf->parent;
		candleaf->key = candleaf->left->key;
		tmp_ptr = candleaf->left;
		return_node(candleaf->right);
		candleaf->left = tmp_ptr->left;
		candleaf->right = tmp_ptr->right;
		return_node(tmp_ptr);
		if (candleaf->right == NULL)
			candleaf->height = 0;
		else{
			candleaf->left->parent = candleaf;
			candleaf->right->parent = candleaf;
			candleaf->height = 1;
		}
		l_o_t_rebalance(candleaf);
	}
	else { //candleaf->parent-Left == candleaf
		candleaf=candleaf->parent;
		candleaf->key = candleaf->right->key;
		tmp_ptr = candleaf->right;
		return_node(candleaf->left);
		candleaf->left = tmp_ptr->left;
		candleaf->right = tmp_ptr->right;
		return_node(tmp_ptr);
		
		if (candleaf->right == NULL)
			candleaf->height = 0;
		else{
			candleaf->left->parent = candleaf;
			candleaf->right->parent = candleaf;
			candleaf->height = 1;
		}
		l_o_t_rebalance(candleaf);
	}
	
	//delete node from o_t (binary tree)
	if (previous->right == current_node){
		previous->key = previous->left->key;
		previous->height = 0;
		return_ot_node(previous->right);
		previous->right=NULL;
		tmp_node = previous->left->left;
		return_ot_node(previous->left);
		previous->left = tmp_node;
	}
	else{//previous->left==current_node
		previous->key = previous->right->key;
		previous->height = 0;
		return_ot_node(previous->left);
		tmp_node = previous->right->left;
		return_ot_node(previous->right);
		previous->left = tmp_node;
		previous->right = NULL;
	}
	path_st_p--;
	//update the o_t pointer for the parent of a 
	o_t *update_ptr = ord;
	while( update_ptr->right != NULL ){
		if( candleaf->key < update_ptr->key )
			update_ptr = update_ptr->left;
		else
			update_ptr = update_ptr->right;
	}
	update_ptr->left = (o_t*) candleaf;

	rebalance(path_stack, path_st_p);
}

int compare(o_t *ord, key_t a, key_t b){
	o_t *a_ptr, *b_ptr;
	l_o_t *apath, *bpath, *achild;
	a_ptr = b_ptr = ord;
	apath = bpath = achild = NULL;

	//find a and b in the binary treee
	while( a_ptr->right != NULL ){ 
		if( a < a_ptr->key ){
			a_ptr = a_ptr->left;
		}
		else{
			a_ptr = a_ptr->right;
		}
	}

	while( b_ptr->right != NULL ){ 
		if( b < b_ptr->key ){
			b_ptr = b_ptr->left;
		}
		else{
			b_ptr = b_ptr->right;
		}
	}

	apath = (l_o_t*) a_ptr->left;
	bpath = (l_o_t*) b_ptr->left;

	while (apath != bpath){
		if (apath->height == bpath->height){
			achild = apath;
			apath = apath->parent;
			bpath = bpath->parent;
		}
		else if (apath->height > bpath->height){
			bpath = bpath->parent;

		}
		else{ //apath->height < bpath->height 
			achild = apath;
			apath = apath->parent;
		}
	}
		
	if (apath->left == achild)
		return 1;	
	else 
		return 0;
}

long p(long q)
{ return( (1247*q +104729) % 300007 );
}

int main(){
	long i; o_t *o; 
   printf("starting \n");
   o = create_order();
   for(i=100000; i>=0; i-- )
      insert_bottom( o, p(i) );
   for(i=100001; i< 300007; i+=2 )
   {  insert_after(o, p(i+1), p(i-1) );
      insert_before( o, p(i), p(i+1) );
   }
   printf("inserted 300000 elements. ");
   for(i = 250000; i < 300007; i++ )
      delete_o( o, p(i) );
   printf("deleted 50000 elements. ");
   insert_top( o, p(300006) );
   for(i = 250000; i < 300006; i++ )
      insert_before( o, p(i) , p(300006) );
   printf("reinserted. now testing order\n");
   for( i=0; i < 299000; i +=42 )
   {  if( compare( o, p(i), p(i+23) ) != 1 )
      {  printf(" found error (1) \n"); exit(0);
      }
   }
   for( i=300006; i >57; i -=119 )
   {  if( compare( o, p(i), p(i-57) ) != 0 )
      {  printf(" found error (0) \n"); exit(0);
      }
   }
   printf("finished. no problem found.\n");
}