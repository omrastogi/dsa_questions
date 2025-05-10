from typing import List

class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        voids1 = nums1.count(0)
        voids2 = nums2.count(0)
        
        # add voids to sum as the minimum sum will be taken after replacing 0 by 1
        sum1 = sum(nums1) + voids1
        sum2 = sum(nums2) + voids2
        
        if sum1 < sum2:
            if voids1 > 0:
                return sum2
            else:
                return -1
        elif sum1 > sum2:

            if voids2 > 0:
                return sum1
            else:
                return -1
        else:
            return sum1
    
if __name__ == "__main__":
    nums1 = [3,2,0,1,0]
    nums2 = [6,5,0]
    solution = Solution()
    print(solution.minSum(nums1, nums2))
