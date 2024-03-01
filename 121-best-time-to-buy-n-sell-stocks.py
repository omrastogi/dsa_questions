from typing import List

class Solution0:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        N = len(prices)
        for i in range(N):
            for j in range(i+1, N):
                max_profit = max(prices[j] - prices[i], max_profit)

        return max_profit
                
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = float('inf')
        N = len(prices)
        # i, j = 0, 1
        for i in range(N):
            if min_val > prices[i]:
                min_val = prices[i]
                continue
            else:
                max_profit = max(prices[i] - min_val, max_profit)

        return max_profit

if __name__ == "__main__":
    obj = Solution()
    ss = [[7,1,5,3,6,4]]
    for s in ss:
        print(obj.maxProfit(s))