from typing import Optional, List

class Solution:
    def __init__(self):
        self.subset_list = []
    
    def dfs(self, index, path, nums):
        """
        Backtracking function to generate all subsets.

        Parameters:
        - index: The current position in the nums array.
        - path: The current subset being built.
        - nums: The input array of unique elements.

        """
        
        # ✅ Step 1: Store the current subset (including the empty one at the start)
        self.subset_list.append(path[:])  # [:] creates a copy to prevent modification issues

        # ✅ Step 2: Loop through the remaining elements
        for i in range(index, len(nums)):  
            # Include nums[i] in the current subset
            path.append(nums[i])

            # ✅ Step 3: Recursive call to generate further subsets
            # Move to the next index (i + 1) to avoid duplicates
            self.dfs(i + 1, path, nums)

            # ✅ Step 4: Backtrack to remove the last added element and explore new subsets
            path.pop()


    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.dfs(0, [], nums)
        return self.subset_list
    

if __name__ == "__main__":
    nums = [1, 2, 3]  # ✅ Random input
    solution = Solution()
    result = solution.subsets(nums)
    print("All subsets:", result)
        

