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

class RBTree:
    def __init__(self):
        self.root = None
    
    # -------- Insert (recursive) --------
    def insert_recurse(self, key):
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
        if self.root is None:
            return Node(key)

        if key < self.root.key:
            child = self.insert_recurse(self.root.left, key)
            self.root.left = child
            child.parent = self.root
        else:
            child = self.insert_recurse(self.root.right, key)
            self.root.right = child
            child.parent = self.root

    # -------- Insert (iterative) --------
    def insert(self, z):
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
        curr = self.root 
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
            self.root = child 
        else:
            if z < parent.key:
                parent.left = child
            else:
                parent.right = child 

    # -------- Search --------
    def search(self, val):
        """Iterative search from self.root."""
        curr = self.root
        while curr is not None and curr.key != val:
            curr = curr.left if val < curr.key else curr.right
        return curr
    
    # -------- Min / Max --------
    def tree_min(self, root=None):
        """Return min node starting at root (default: self.root)."""
        curr = self.root if root is None else root
        if curr is None:
            return None
        while curr.left is not None:
            curr = curr.left
        return curr

    def tree_max(self, root=None):
        """Return max node starting at root (default: self.root)."""
        curr = self.root if root is None else root
        if curr is None:
            return None
        while curr.right is not None:
            curr = curr.right
        return curr

    # -------- Successor --------
    def successor(self, node):
        """In-order successor of node."""
        if node is None:
            return None
        if node.right is not None:
            return self.tree_min(node.right)
        parent = node.parent
        while parent is not None and node is parent.right:
            node = parent
            parent = parent.parent
        return parent

    # -------- Transplant (helper for delete) --------
    def transplant(self, tar, rep):
        """
        Input:
            tar (Node): The target node to be replaced
            rep (Node): The replacement node to place in the node2's position

        Replace subtree rooted at tar with subtree rooted at rep.
        Updates parents and self.root accordingly.
        """
        # check if target is root node
        if tar.parent is None:
            self.root = rep
        # check if target is left and right to replace accordingly
        elif tar is tar.parent.left:
            tar.parent.left = rep
        else:
            tar.parent.right = rep
        # set the parent pointer after replacing the new node
        if rep is not None:
            rep.parent = tar.parent

    # -------- Deletion --------
    def deletion(self, node):
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
        # If node is None
        if node is None:
            return
        # if node has only the right child
        if node.left is None:
            self.transplant(node, node.right)
        # if node has only the left child
        elif node.right is None:
            self.transplant(node, node.left)
        # if node has both child 
        else:
            y = self.tree_min(node.right)         # successor of node
            if y.parent is not node:
                self.transplant(y, y.right)
                # setting the right side of node
                y.right = node.right # set the right pointer of y
                if y.right is not None:
                    y.right.parent = y # set the parent pointer in right child 
            
            self.transplant(node, y)
            y.left = node.left
            if y.left is not None:
                y.left.parent = y # set the  the parent pointer of the left child

    # -------- Traversals --------
    # Inorder traversal (Left → Root → Right)
    def inorder(self, root=None):
        """Return in-order list of keys (recursive)."""
        res = []
        def _dfs(n):
            if n is None:
                return
            _dfs(n.left)
            res.append(n.key)
            _dfs(n.right)
        _dfs(self.root if root is None else root)
        return res

    def inorder_loop(self, root=None):
        """Return in-order list of keys (iterative)."""
        stack, order, curr = [], [], (self.root if root is None else root)
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            order.append(curr.key)
            curr = curr.right
        return order


    # -------- Rows for visualization --------
    def build_rows(self, root=None):
        """Return level rows incl. None placeholders for visualization."""
        root = self.root if root is None else root
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
    t = RBTree()
    for k in [50,30,20,40,70,60,80,90,75,55,65]:
        t.insert(k)

    print(t.inorder_loop())          # in-class traversal
    n = t.search(70)
    t.deletion(n)                    # delete node 70







