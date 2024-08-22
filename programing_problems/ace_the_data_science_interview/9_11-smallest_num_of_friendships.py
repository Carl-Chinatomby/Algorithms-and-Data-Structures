"""
Ace The Data Science Interview


Medium Problems
9.11. Facebook: You have the entire social graph of Facebook users, with nodes representing users
and edges representing friendships between users. Given a social graph and two users as
input, write a function to return the smallest number of friendships, between two users. For
example, take the graph that consists of 5 users A, B, C, D, E and the friendship edges are:
(A, B), (A, C), (B, D), (D, E). If the two input users are A and E, then the function should return 3
since A is friends with B, B is friends with D, and D is friends with E.
"""
from collections import defaultdict
import queue

def smallest_num_of_friendships(edges, x, y):
    # Build edge_map
    edge_map = defaultdict(list)
    for vert1, vert2 in edges:
        edge_map[vert1].append((vert1, vert2))
        #edge_map[vert2].append((vert2, vert1))

    #visted = {}
    def dist_helper(edge_map, source, destination):
        distances = []
        print(source, destination)
        for vert1, vert2 in edge_map[source]:
            #visited[(vert1, vert2)] = True
            #visited[(vert2, vert1)] = True
            if vert2 == destination:
                return 1
            elif vert2 in edge_map:
                cur_distance = 1 + dist_helper(edge_map, vert2, destination)
                distances.append(cur_distance)
        return min(distances) if distances else 0

    return dist_helper(edge_map, x, y)

def smallest_num_of_friendships(edges, x, y):
    n = len(edges)
    distance = [0] * n # distances from x
    processed = [False] * n # visited or not already
    q = queue.Queue()
    q.put(x)
    processed[x] = True
    while (not q.empty()):
        curr = q.get()
        if curr not in edges:
            continue
        for neighbor in range(len(edges[curr])): # process if not visited
            distance[edges[curr][neighbor]] = distance[curr] + 1
            q.put(edges[curr][neighbor]) # add neighbor
            processed[edges[curr][neighbor]] = True
    return distance[y]


if __name__ == "__main__":
    #relationships = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('D', 'E')]
    relationships = {
         0: [1, 2],
         1: [3],
         2: [],
         3: [4],
         4: []s
    }
    #user_1 = 'A'
    #user_2 = 'E'
    user_1 = 0
    user_2 = 4
    expected_value = 3

    # we need to check if there is a direct

    actual_value = smallest_num_of_friendships(relationships, user_1, user_2)
    print("Test 1: ", actual_value == expected_value,
        "actual: ", actual_value,
        "expected: ", expected_value
    )
