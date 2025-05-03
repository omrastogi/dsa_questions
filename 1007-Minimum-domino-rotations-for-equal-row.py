from collections import defaultdict
from typing import List

class Solution0:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # First count the values in top and bottom dominos
        total_cnt = defaultdict(int)
        max_num = float('-inf')
        for top, btm in zip(tops, bottoms):
            if top != btm:
                total_cnt[top] += 1
            total_cnt[btm] += 1
        max_key = max(total_cnt, key=total_cnt.get)
        if len(tops) != total_cnt[max_key]:
            return -1 
        top_cnt, btm_cnt = 0, 0
        for top, btm in zip(tops, bottoms):
            if top == btm:
                continue
            elif top == max_key:
                top_cnt += 1 
            else:
                btm_cnt += 1 
        
        return min(top_cnt, btm_cnt)

# VVIP for the question
# If a number can fill all positions after rotations, it must appear in every domino either top or bottom — so only tops[0] and bottoms[0] are valid candidates to check.
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            top_swaps = bottom_swaps = 0
            for a, b in zip(tops, bottoms):
                if a != x and b != x:
                    return float('inf')
                elif a != x:
                    top_swaps += 1
                elif b != x:
                    bottom_swaps += 1
            return min(top_swaps, bottom_swaps)

        res = min(check(tops[0]), check(bottoms[0]))
        return res if res != float('inf') else -1


if __name__ == "__main__":
    obj = Solution()
    tops = [2,1,2,4,2,2]
    bottoms = [5,2,6,2,3,2]
    print(obj.minDominoRotations(tops, bottoms))

