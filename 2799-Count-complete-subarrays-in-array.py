from typing import List

class Solution0:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique_ele = []
        for num in nums:
            if num not in unique_ele:
                unique_ele.append(num)
        k = len(unique_ele)
        N = len(nums)
        cnt = 1
        for sz in range(k, N):
            for start in range(0, N-sz+1):
                subset = nums[start:start+sz]
                ele = []
                for num in subset:
                    if num not in ele:
                        ele.append(num)
                if len(ele)==k:
                    # print(subset)
                    cnt += 1
        return cnt

class Solution1:
    @staticmethod
    def check_complete_subset(subset, k):
        ele = []
        for num in subset:
            if num not in ele:
                ele.append(num)
        return len(ele) == k

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        unique_map = {}
        for num in nums:
            if num not in unique_map:
                unique_map[num] = 1
            else:
                unique_map[num] += 1
        k = len(unique_map)
        if k == 1:
            return sum([i+1 for i in range(N)])
        min_freq = min(unique_map.values())
        min_freq_num = next(num for num in unique_map if unique_map[num] == min_freq)
        min_freq_indices = [i for i, num in enumerate(nums) if num == min_freq_num]
        cnt = 1
        for sz in range(N-1, k-1, -1):
            for start in range(N-sz+1):
                # # Skip if all min frequency elements are outside the current window
                if all(idx < start or idx >= start+sz for idx in min_freq_indices):
                    continue
                subset = nums[start:start+sz]
                # print(subset)   
                if self.check_complete_subset(subset, k):
                    # print(subset)
                    cnt += 1
        return cnt

from collections import defaultdict
class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        total_unique = len(set(nums))
        count = 0
        n = len(nums)

        for i in range(n):
            freq = defaultdict(int)
            unique_count = 0
            for j in range(i, n):
                if freq[nums[j]] == 0:
                    unique_count +=1
                freq[nums[j]] += 1 
                if unique_count == total_unique:
                    count += 1
                
        return count

if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        [1, 3, 1, 2, 2],
        [381,1304,381,758,1304,381,758],
        [5, 5, 5, 5],
        [1, 2, 3, 4]
    ]
    
    for nums in test_cases:
        result = sol.countCompleteSubarrays(nums)
        print(f"Complete subarrays in {nums}: {result}")
        # break
