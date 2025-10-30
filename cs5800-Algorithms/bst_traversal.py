from collections import deque

class Node:
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
    
    def __repr__(self):
        cls = self.__class__.__name__
        parent_key = self.parent.key if self.parent else None
        left_key = self.left.key if self.left else None
        right_key = self.right.key if self.right else None
        return f"{cls}(key={self.key}, left={left_key}, right={right_key}, parent={parent_key})"

# Insert a new key into the BST
def insert_recurse(root, key):
    """
    Recursive BST insert that also sets parent pointers.

    Complexity:
      - Time:  O(h), where h is the tree height.
      - Space: O(h) extra on the Python call stack.

    Notes:
      - Recursion can hit Python's recursion limit (~1000) on skewed trees.
        Prefer the iterative version for robustness and O(1) extra space.
    
    Duplicate policy: 
      - keys equal to `root.key` are inserted to the RIGHT.
    """
    if root is None:
        return Node(key)

    if key < root.key:
        child = insert(root.left, key)
        root.left = child
        child.parent = root
    else:
        child = insert(root.right, key)
        root.right = child
        child.parent = root
    return root

def insert(root, z):
    """
    Iterative BST insert

    Complexity:
      - Time:  O(h), where h is the tree height.
      - Space: O(1)

    Duplicate policy: 
      - keys equal to `root.key` are inserted to the RIGHT.
    """
    # find the parent to insert under
    parent = None 
    curr = root 
    while curr != None:
        parent = curr 
        if z < curr.key:
            curr = curr.left
        else:
            curr = curr.right 

    # create a Node for key
    child = Node(key=z, parent=parent)

    # Deciding the position of new element wrt child
    if parent is None:
        root = child 
    else:
        if z < parent.key:
            parent.left = child
        else:
            parent.right = child 
    return root

def search(node, val):
    if node==None or val==node.val:
        return node 
    if val < node.key:
        return search(node.left, k)
    else:
        return search(node.right, k)
    
def tree_min(root):
    curr = root
    while curr.left is not None:
        curr = curr.left 
    return curr

def tree_max(root):
    curr = root 
    while curr.right is not None:
        curr = curr.right 
    return curr

def successor(node):
    """
    Input:
        node (Node): A node in a Binary Search Tree (BST) with 'left', 'right', and 'parent' pointers.
    Output:
        Node: The in-order successor of the given node — i.e., the node with the smallest key
              greater than the key of the input node. Returns None if no successor exists.
    """
    if node.right is not None:
        return tree_min(node.right)
    parent = node.parent
    while parent is not None and node == parent.right:
        node = parent
        parent = parent.parent
    return parent

# Inorder traversal (Left → Root → Right)
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

def inorder_loop(root):
    stack, order, curr = [], [], root
    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        print(curr)
        order.append(curr.key)
        curr = curr.right
    return order
            

# Example usage
if __name__ == "__main__":
    keys = [50, 30, 20, 40, 70, 60, 80]
    root = None
    for k in keys:
        root = insert(root, k)

    print("Inorder traversal of BST:")
    print(inorder_loop(root))
