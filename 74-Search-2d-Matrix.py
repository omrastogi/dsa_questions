from typing import List

class Solution:
    def __init__(self):
        self.trows, self.tcols = None, None
        self.matrix = None 

    def get_ele(self, index):
        row = index // self.tcols
        col = index % self.tcols
        return self.matrix[row][col]

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        self.trows, self.tcols = len(matrix), len(matrix[0])
        self.matrix = matrix
        i, j = 0, (self.trows * self.tcols) - 1  # ✅ Correct initialization

        while i <= j:  # ✅ Correct binary search condition
            mid = (i + j) // 2
            if self.get_ele(mid) < target:
                i = mid + 1  # ✅ Move right
            elif self.get_ele(mid) > target:
                j = mid - 1  # ✅ Move left
            else:
                return True  # Found target

        return False  # Target not found

if __name__ == "__main__":
    # Example matrix and test cases
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    targets = [3, 34, 13, 60]  # Testing multiple targets
    
    solution = Solution()
    
    for target in targets:
        result = solution.searchMatrix(matrix, target)
        print(f"Target {target}: {'Found' if result else 'Not Found'}")

