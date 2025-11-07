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

def deletion(root, node):
    """
    Input:
        root: The Root node in BST with 'left', 'right', and 'parent' pointers
        node (Node): The node that is to be deleted

    Three cases:
    1. If z has no children 
        - Just remove it 
    2. If z has just one child
        - make the child take the position of z in the subtree dragging it's child's subtree along 
    3. If z has two children
        - find the the successor of z (y) and replace z by y in the tree
            - y must be in right subtree of z and have no left child 
            - rest of the original subtree of z becomes the new right subtree of y 
            - The left subtree of z becomes the new left subtree of y 
    """
    # if node has only the right child
    if node.left is None:
        transplant(root, node, node.right)
    # if node has only the left child
    elif node.right is None: 
        transplant(root, node, node.left)
    # if node has both child 
    else:
        y = tree_min(node.right) # successor of node
        if y.parent != node:
            transplant(root, y, y.right)
            # setting the right side of node
            y.right = node.right # set the right pointer of y
            y.right.parent = y # set the parent pointer in right child 
        
        transplant(root, node, y)
        y.left = node.left
        y.left.parent = y # set the  the parent pointer of the left child



def transplant(root, tar, rep):
    """
    Input:
        root (Node): The Root node in BST with 'left', 'right', and 'parent' pointers
        tar (Node): The target node to be replaced
        rep (Node): The replacement node to place in the node2's position
    """
    # check if target is root node
    if tar.parent is None:
        root = rep
    else:
        # check if target is left and right to replace accordingly
        if tar == tar.parent.left:
            tar.parent.left = rep
        else:
            tar.parent.right = rep
    # set the parent pointer after replacing the new node
    if rep is not None:
        rep.parent = tar.parent
    
    return root


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

def build_rows(root):
    """Return rows of nodes including None placeholders so that:
       rows[i][j] -> children are rows[i+1][2*j], rows[i+1][2*j+1]."""
    if not root:
        return []
    rows = [[root]]
    while True:
        prev = rows[-1]
        nxt, any_real = [], False
        for n in prev:
            if n is None:
                nxt.extend([None, None])
            else:
                nxt.append(n.left)
                nxt.append(n.right)
                any_real |= (n.left is not None or n.right is not None)
        if not any_real:
            break
        rows.append(nxt)
    return rows


# Example usage
if __name__ == "__main__":
    from binary_search_trees.bst_visualization import render_ascii_tree
    keys = [50, 30, 20, 40, 70, 60, 80, 90, 75, 55, 65]
    root = None
    for k in keys:
        root = insert(root, k)

    print("Inorder traversal of BST:")
    print(inorder_loop(root))
    print()
    render_ascii_tree(root)
    deletion(root, root.right)
    print()
    render_ascii_tree(root)
