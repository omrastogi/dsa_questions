from collections import defaultdict
from typing import List

class Solution0:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        k = defaultdict(int)
        for domino in dominoes:
            if domino[0] > domino[1]:
                domino = domino[::-1]
            domino = str(domino[0])+str(domino[1])
            # print(domino)
            k[domino] += 1
        
        cnt = 0
        for _, n in k.items():
            cnt += int((n * (n-1)) / 2)
        
        return cnt

# works better by using tuple
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        k = defaultdict(int)

        for a, b in dominoes:
            key = tuple(sorted((a, b)))  # always (min, max)
            k[key] += 1

        cnt = 0
        for n in k.values():
            cnt += n * (n - 1) // 2  # use integer division

        return cnt

if __name__ == "__main__":
    obj = Solution()
    dominoes = [[1,2],[2,1],[3,4],[5,6]]
    print(obj.numEquivDominoPairs(dominoes))  # Expected: 1
    
    dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    print(obj.numEquivDominoPairs(dominoes))  # Expected: 3
