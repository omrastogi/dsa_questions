from typing import List

#-------------- Wrong Solution -------------------------
class Solution:
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
class Solution:
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

            
if __name__ == "__main__":
    obj = Solution()
    ss = [([1,2], [3,4,5,6,7])]
    for s in ss:
        print(obj.findMedianSortedArrays(s[0], s[1]))



