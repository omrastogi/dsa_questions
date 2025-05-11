from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        p1 = p2 = -1
        for i, num in enumerate(arr):
            if num % 2:
                p2 = i 
            else:
                p1 = i
            if p2 - p1 >= 3:
                return True 
        return False
    
if __name__ == "__main__":
    solution = Solution()
    arr1 = [2,6,4,1]  # False
    arr2 = [1,2,34,3,4,5,7,23,12]  # True
    arr3 = [1,3,5,7]  # True
    
    print(solution.threeConsecutiveOdds(arr1))
    print(solution.threeConsecutiveOdds(arr2))
    print(solution.threeConsecutiveOdds(arr3))
