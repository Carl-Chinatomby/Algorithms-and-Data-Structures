/*
 * ************************
 * By Carl Chinatomby
 * ************************
 * FALL 2009 Algorithms Morning Section Tues/Thurs
 * HW#3 - Dijkstra's Algorithm
 * 
 * Assignment: Implement Dijkstra's shortest path
 * algorithm for the prototype:
 * 
 * struct listnode shortest_path(int v, int s, int t, int *dist)
 * where dist is the distance matrix A[v][v]
 * s is the start node
 * t is the target node
 * and v is the number of vertices 
*/
#include <iostream>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstdio>
using namespace std;

struct listnode { struct listnode *next; int vertexnumber; };

struct listnode shortest_path(int v, int s, int t, int *dist)
{	//declarations and initilizations
	const int INF=9999; 	
	int i=0;
	int *pathLength = new int[v];	int *previous = new int[v];		bool* visited=new bool[v];	//pathLength, pathtracker, and visited node
	int currentV=s;	int currentVdist=INF;	int nextV;	int nextVdist=INF;
	for (i=0; i<v; i++) { pathLength[i] = INF;previous[i]=INF; visited[i]=0;}
	pathLength[s] = 0; //dist to itself is always 0
	previous[s]=s;	//path tracker
	
	//fillup distance table and track paths
	while (currentV != t)
	{
		for (i=0; i < v; i++) {
			visited[currentV] = true;
			currentVdist=*(dist+v*currentV+i) + pathLength[currentV];
			if ((currentVdist < (pathLength[i]))){
				pathLength[i]=currentVdist;
				previous[i]=currentV;		
			}
			if(*(dist+v*currentV+i) < nextVdist && !visited[i]){ 
				nextV = i;
				nextVdist= *(dist+v*currentV+i);
			}
		}
		currentV=nextV;
		nextVdist=INF;
	}
	//create linked list of path
	listnode* path=NULL;
	listnode* tmp=NULL;
	for (i=t; i!=s; i=previous[i])	{tmp = path; path = new listnode; path->vertexnumber=i; path->next =tmp; }
	tmp = path; path = new listnode; path->vertexnumber=i; path->next =tmp;
	return *path;
}

int dist[1000][1000];
int main(void)
{ 
   /*
    This is the Professor's test code. Scores were either pass
    or fail depending on the time complexity of the program
    and having the correct shortest path. The correct path is:
    0, 128, 500, 900, 999
   */
   int i,j;
   struct listnode tmpx, *tmp;
   for(i=0; i< 1000; i++)
     for( j =0; j< 1000; j++ )
     {  if( i<500 && j<500 )
           dist[i][j] = 110 + ((i*i +j*j + 13*(i+j) )%20);
        else
           dist[i][j] = 200 + ((i*i +j*j + 13*(i+j) )%20);
     }


   for(i=0; i< 1000; i++)
     dist[i][i]=0;
   for(i=0; i< 100; i++)
   {  dist[i][2*i+1] = 15; dist[2*i+1][i] = 15;
      dist[i][2*i+2] = 15; dist[2*i+2][i] = 15;
   }
   dist[0][128] = 100; dist[128][0]=100;
   dist[128][500] = 1; dist[500][128]= 1;
   for( i = 0; i< 100; i++)
   {  dist[300+ (7*i)%100][300+(7*i+7)%100] = 1; 
      dist[300+ (7*i+7)%100][300+(7*i)%100] = 1; 
      dist[300+i][450] = 2; dist[450][300+1] = 2;
   }
   for(i=502; i<900; i++)
   { dist[450][i] = 3; dist[i][450]=3;
     dist[500][i] = 2;   dist[i][500]=2;
     dist[501][i] = 10; dist [i][501] = 10;
   }
   dist [500][900] = 50; dist[900][500]=50;
   dist [899][900] = 49; dist[899][900]=49;
   dist [900][999] = 1; dist [999][900] = 1;
   printf("constructed distance matrix for graph with 1000 vertices\n");
   tmpx =  shortest_path(1000, 0, 999, &dist[0][0]);
   tmp = & tmpx;
   printf("The shortest path from 0 to 999 uses the vertices\n");
   while( tmp != NULL )
   {  printf("%d, ", tmp->vertexnumber);
      tmp = tmp->next;
   }
   printf("End test\n");
   exit(0);
}
