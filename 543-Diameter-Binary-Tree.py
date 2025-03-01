from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0 

    def get_depth(self, root):
        if root is None:
            return 0

        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        
        self.diameter = max(self.diameter, (left_depth + right_depth))
        return 1 + max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_depth(root)
        return self.diameter

if __name__ == "__main__":
    # Constructing the binary tree
    #        1
    #       / \
    #      2   3
    #     / \   \ 
    #    5   6   4
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)

    # Creating Solution instance and calling the function
    solution = Solution()
    result = solution.diameterOfBinaryTree(root)

    # Print the output
    print("Diameter of the Binary Tree:", result)
