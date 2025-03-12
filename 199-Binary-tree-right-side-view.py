from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        output = []
        
        while queue:
            output.append(queue[-1].val)  # Last node at this level
            
            for _ in range(len(queue)):  # Process all nodes at this level
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return output

# Hardcoded binary tree input
def main():
    # Constructing the binary tree:
    #         1
    #        / \
    #       2   3
    #        \   \
    #         5   4
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    solution = Solution()
    result = solution.rightSideView(root)
    print("Right Side View:", result)

if __name__ == "__main__":
    main()
