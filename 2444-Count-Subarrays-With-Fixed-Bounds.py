from typing import List 

class Solution0:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        N = len(nums)
        subarrays = []
        for i in range(N):
            check_min, check_max = False, False
            if nums[i] == minK:
                check_max = True
            elif nums[i] == maxK:
                check_min = True
            fsbF = False
            for j in range(i, N):
                if nums[j] > maxK or nums[j] < minK:
                    break
                if (nums[j] == maxK and check_max) or (nums[j] == minK and check_min):
                    print(nums[j])
                    fsbF = True
                if fsbF:
                    subarrays.append(nums[i:j+1])
        for sub in subarrays:
            print(sub)
        return len(subarrays)

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        last_bad, last_max, last_min = -1, -1, -1
        for i, num in enumerate(nums):
            if num>maxK or num<minK:
                last_bad = i 
            if num==maxK:
                last_max = i 
            if num==minK:
                last_min = i
            res += max(0, min(last_min, last_max) - last_bad)

        return res
            
            

             

if __name__ == "__main__":
    nums = [1,3,5,2,7,5]
    minK = 1
    maxK = 5
    sol = Solution()
    print(sol.countSubarrays(nums, minK, maxK))
