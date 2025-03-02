from typing import List

class Solution:
    def __init__(self):
        self.combinations = []

    def dfs(self, index, path, remain, nums):
        if remain == 0:
            self.combinations.append(path[:])
        elif remain < 0:
            return
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(i, path, remain - nums[i], nums)  # Reuse candidates by passing i
            path.pop()
         
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.dfs(0, [], target, candidates)
        return self.combinations

if __name__ == "__main__":
    # Hardcoded test case:
    sol = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    result = sol.combinationSum(candidates, target)
    print("Candidates:", candidates)
    print("Target:", target)
    print("Combinations:", result)
