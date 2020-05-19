# Libraries Included:
# Numpy, Scipy, Scikit, Pandas
# 
# Old Content below(Python 2):
# 
# # Libraries Included:
# # Numpy, Scipy, Scikit, Pandas
# 
# print "Hello, world!"
import uuid
import unittest
from copy import deepcopy

class Node():
    def __init__(self, children=None):
        self.id = uuid.uuid4()
        if children == None:
            self.children = []
        else:
            self.children = children
            
    def add_child(self, node):
        self.children.append(node)
        
    def add_children(self, nodes):
        self.children.extend(nodes)
    
def get_children(root):
    remaining_nodes = [root]
    while remaining_nodes:
        current_node = remaining_nodes.pop()
        yield current_node
        for child in current_node.children:
            remaining_nodes.append(child)
    
def calculate_height(root):
    current_node = root
    count = -1 # do not count root
    
    if current_node is None:
        return 0
    
    for node in get_children(current_node):
        count += 1
    
    return count

def has_cycle(root):
    if not root or not root.children:
        return False
    
    has_visited = {}
    
    for current_node in get_children(root):
        if has_visited.get(current_node.id):
            return True

        has_visited[current_node.id] = True
    
    return False


def create_loop_nodes():
    base_node = Node()
    circular_node = Node(children=[base_node])
    base_node.add_child(circular_node)
    return base_node

def generate_nodes(n):
    return [Node() for i in range(n)] 

class TestHasCycle(unittest.TestCase):
    def generate_nodes(self, n):
        return [Node() for i in range(n)]      
    
    def setUp(self):
        self.circular = Node(
        children=[
            create_loop_nodes(),
        ])
        self.circular.add_children(generate_nodes(8))
        self.circular.children[0].add_children(generate_nodes(3))
            
        self.non_circular = Node()
        self.non_circular.add_children(generate_nodes(8))
        self.non_circular.children[0].add_children(generate_nodes(3))
    
    def test_empty_root_returns_false(self):
        self.assertFalse(has_cycle(None))
    
    def test_single_node_returns_false(self):
        self.assertFalse(has_cycle(Node()))
    
    def test_node_with_multiple_children_for_cycles(self):
        self.assertTrue(has_cycle(self.circular))
        self.assertFalse(has_cycle(self.non_circular))
    
    def test_node_with_multiple_nested_children_for_cycle(self):
        circular_nested = deepcopy(self.circular)
        circular_nested.children[1].add_children(generate_nodes(8))
        self.assertTrue(has_cycle(circular_nested))
        
        non_circular_nested = deepcopy(self.non_circular)
        non_circular_nested.children[1].add_children(generate_nodes(8))
        self.assertFalse(has_cycle(non_circular_nested))
    

def main():
    node1 = Node()
    node2 = Node(children=[node1])
    node1.add_child(node2)
    
    root = Node(
        children=[
            node1,
            Node(children=[Node()]),
            Node()
        ]
    )
    
    root2 = Node(
        children=[
            Node(),
            Node(children=[Node()]),
            Node()
        ]
    )
            
            
    print(calculate_height(root))
    print(has_cycle(root2))

#main()
unittest.main()