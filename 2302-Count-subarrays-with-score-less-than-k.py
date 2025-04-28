from typing import List

class Solution0:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        N = len(nums)
        # print(nums)
        sqrt_k = min(int(k ** 0.5), N+1)
        cnt = 0
        for lngt in range(1, sqrt_k+1):
            for i in range(N-lngt+1):
                if sum(nums[i:i+lngt]) * lngt < k:
                    cnt += 1

        return cnt 
    

class Solution1:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        cnt = 0
        for i in range(0, N):
            score = nums[i]
            if score < k: 
                print(nums[i])
                cnt += 1 
            else:
                continue
            for j in range(i+1, N):
                n = j - i + 1 
                score = (nums[j] + (score // (j - i))) * n
                if score < k:
                    print(nums[i:j+1])
                    cnt += 1 
                else:
                    break 
        # if sum(nums) * N < k:
        #     cnt += 1
        return cnt 

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        l = 0
        cur_sum = 0
        cnt = 0
        
        for r in range(N):
            cur_sum += nums[r]
            while l <= r and cur_sum * (r - l + 1) >= k:
                cur_sum -= nums[l]
                l += 1
            cnt += (r - l + 1)
        
        return cnt

if __name__ == "__main__":
    # Hardcoded input
    nums = [1, 1, 1]
    k = 9
    sol = Solution()
    result = sol.countSubarrays(nums, k)
    print("Count of subarrays with score less than k:", result)
