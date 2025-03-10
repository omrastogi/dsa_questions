from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Implementation of BFS
        queue = deque([root])
        while queue:
            current = queue.popleft()
            if not current:
                continue
            queue.extend([current.right, current.left])
            current.right, current.left = current.left, current.right
        
        return root

# Helper function to print the tree (level order)
def level_order_traversal(root):
    if not root:
        return []
    queue = deque([root])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    return result

# Main gate
if __name__ == "__main__":
    # Hardcoded input: [4,2,7,1,3,6,9]
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Original Tree:", level_order_traversal(root))
    
    solution = Solution()
    inverted_root = solution.invertTree(root)
    
    print("Inverted Tree:", level_order_traversal(inverted_root))
