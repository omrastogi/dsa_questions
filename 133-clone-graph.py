from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.vals = {}
    def copyNode(self, node):
        if node.val in self.vals.keys():
            return self.vals[node.val]
        newnode = Node(node.val)
        self.vals[node.val] = newnode  
        newnode.neighbors = [None] * len(node.neighbors)
        for i, neighbor in enumerate(node.neighbors):
            newnode.neighbors[i] = self.copyNode(neighbor)
        return newnode


    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        newnode = self.copyNode(node)        
        return newnode
    
class Bfs_Solution:
    def __init__(self):
        self.vals = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        # Initialize BFS queue and clone the first node
        queue = deque([node])
        self.vals[node] = Node(node.val)  # Store original_node -> cloned_node mapping

        while queue:
            current = queue.popleft()  # Get the next node in BFS

            # Process neighbors
            for neighbor in current.neighbors:
                if neighbor not in self.vals:  # If neighbor is not cloned yet
                    self.vals[neighbor] = Node(neighbor.val)  # Clone it
                    queue.append(neighbor)  # Enqueue for further processing
                
                # Add cloned neighbor to the current cloned node's neighbors
                self.vals[current].neighbors.append(self.vals[neighbor])

        return self.vals[node]  # Return the cloned version of the starting node

if __name__ == "__main__":
    # Create nodes
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)

    # Connect nodes (Undirected graph)
    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node1, node2]

    # Clone the graph
    solution = Solution()
    cloned_graph = solution.cloneGraph(node1)

    # Print function to verify structure
    def print_graph(node, visited=set()):
        if not node or node in visited:
            return
        visited.add(node)
        print(f"Node {node.val}, Neighbors: {[n.val for n in node.neighbors]}")
        for neighbor in node.neighbors:
            print_graph(neighbor, visited)

    print("Original Graph:")
    print_graph(node1, set())

    print("\nCloned Graph:")
    print_graph(cloned_graph, set())
