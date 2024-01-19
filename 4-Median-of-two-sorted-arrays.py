from typing import List

#-------------- Wrong Solution -------------------------
class SolutionW:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        len1, len2 = len(nums1), len(nums2)
        tlen = len(nums1)+len(nums2)

        if tlen%2:
            indices = [tlen//2 + 1]
        else:
            indices = [tlen//2-1, tlen//2]
        print("indices", indices)
        answer = []
        p1, p2 = 0, 0
        while True:
            if nums1[p1] < nums2[p2]:
                num = nums1[p1]
                if p1>=len1-1:
                    p2+=1
                    num = nums2[p2]
                else:
                    p1+=1

            else:
                num = nums2[p2]
                p2+=1
            print(p1, p2, num, indices)
            if p1+p2 in indices:
                answer.append(num)
                if p1+p2 == indices[-1]:
                    print("ans", answer)
                    return sum(answer)/len(answer)
# ----------------------------------------------------------

                              
# Right Optimized Solution ---------------------------------
# Solution - https://youtu.be/QjrchMRAkew
class Solution0:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m
        N = m + n

        while left <= right:
            A = (left + right) // 2 
            B = ((N + 1) // 2) - A 

            x1 = -float("inf") if A - 1 < 0 else nums1[A - 1]
            y1 = float("inf") if A == m else nums1[A]
            x2 = -float("inf") if B - 1 < 0 else nums2[B - 1]
            y2 = float("inf") if B == n else nums2[B]

            if x1 <= y2 and x2 <= y1:
                if N % 2 == 0:
                    return (max(x1, x2) + min(y1, y2)) / 2
                else:
                    return max(x1, x2)
            elif x1 > y2:
                right = A - 1
            else:
                left = A + 1

# Brute Force Approach -------------------------
# Merge the two arrays together (Similar to merge sort)
class Solution1:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            arr = []
            i, j = 0, 0
            l1, l2 = len(nums1), len(nums2)
            N = l1 + l2
            while True:
                if nums1[i]<=nums2[j]:
                    arr.append(nums1[i])
                    i += 1
                else:
                    arr.append(nums2[j])
                    j += 1 
                if i==l1: 
                    arr.extend(nums2[j:])
                    break 
                if j==l2:
                    arr.extend(nums1[i:])
                    break 

            if N%2:
                return arr[N//2]
            else:
                return (arr[N//2] + arr[(N//2) - 1])/2
            
# Space Optimized Approach -------------------
# The idea is to keep a counter instead of the just keeping the arr
class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
            cnt = 0 
            i, j = 0, 0
            n1, n2 = len(nums1), len(nums2)
            N = n1 + n2
            ind1 = N//2
            ind2 = N//2 - 1
            val1, val2 = -1, -1
            while i < n1 and j < n2 and cnt <= ind1:
                if nums1[i]<=nums2[j]:
                    if cnt == ind1: val1 = nums1[i] 
                    if cnt == ind2: val2 = nums1[1]
                    cnt += 1
                    i += 1
                else:
                    if cnt == ind1: val1 = nums2[j]
                    if cnt == ind2: val2 = nums2[j]
                    cnt += 1
                    j += 1

            while i < n1 and cnt <= ind1:
                if cnt == ind1: val1 = nums1[i] 
                if cnt == ind2: val2 = nums1[i]
                cnt += 1
                i += 1
                
            while j < n2 and cnt <= ind1:
                if cnt == ind1: val1 = nums2[j] 
                if cnt == ind2: val2 = nums2[j]
                cnt += 1
                j += 1
            
            print(N, ind1, ind2)
            print(val1, val2)
            if N%2:
                return val1
            else:
                return (val1 + val2)/2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        
        # We will running binary search on nums1 to create the right partition
        n1, n2 = len(nums1), len(nums2)
        left, right = 0, n1-1
        N = n1 + n2
        if n1 == 0:
            nums1 = nums2 
        while left <= right:
            mid = (left + right) // 2
            cut = ((N) // 2)  - mid

            l1 = -float("inf") if mid - 1 < 0 else nums1[mid - 1]
            r1 = float("inf") if mid == n1 else nums1[mid]
            
            l2 = -float("inf") if cut - 1 < 0 else nums2[cut - 1]
            r2 = float("inf") if cut == n2 else nums2[cut]

            if l1 <= r2 and l2 <= r1:
                if N % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                right = mid - 1
            else:
                left = mid + 1
        

                


if __name__ == "__main__":
    obj = Solution()
    ss = [([1,3], [])]
    for s in ss:
        print(obj.findMedianSortedArrays(s[0], s[1]))



