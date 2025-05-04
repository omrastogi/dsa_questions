from functools import lru_cache
from typing import List

# my code of memoized reccursion
class Solution0:
    def __init__(self):
        self.n = None
        self.prices = None
        self.profit = 0
        self.book = {}

    def dfs(self, i: int, state: int) -> int:
        """
        state: 0 = free, 1 = holding, 2 = cooldown
        returns max profit from day i given the state
        """
        if i == self.n:
            return 0
        
        if (i, state) in self.book:
            return self.book[(i, state)]
        
        price = self.prices[i]
        profit = 0

        if state == 0:
            # I either buy 
            profit1 = -price + self.dfs(i+1, 1)
             # Or I just don't 
            profit2 = self.dfs(i+1, 0)
            # Now we figure out the max 
            profit = max(profit1, profit2)
            
        if state == 1:
            # I either buy 
            profit1 = price + self.dfs(i+1, 2)
            # Or I just don't
            profit2 = self.dfs(i+1, 1)
            # Now we figure out the maximum profit
            profit = max(profit1, profit2)
        
        if state == 2: 
            # I wait 
            profit = self.dfs(i+1, 0)

        # Now I save the profit for furture preferences 
        self.book[(i, state)] = profit

        return profit 

    def maxProfit(self, prices: List[int]) -> int:
        self.n = len(prices)
        self.prices = prices
        return self.dfs(0, 0)

# (by gpt)
class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        @lru_cache(None)
        def dfs(i: int, state: int) -> int:
            """
            state: 0 = free, 1 = holding, 2 = cooldown
            returns max profit from day i given the state
            """
            if i == n:
                return 0

            price = prices[i]

            if state == 0:      # free → buy or skip
                return max(-price + dfs(i + 1, 1),       # buy
                           dfs(i + 1, 0))                # skip
            if state == 1:      # holding → sell or keep
                return max(price + dfs(i + 1, 2),        # sell
                           dfs(i + 1, 1))                # keep holding
            # state == 2        # cooldown → cooldown ends
            return dfs(i + 1, 0)

        return dfs(0, 0)        # start free on day 0

# Best optimized solution (bottom-up DP)
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        hold = -10**18   # f(i,1)
        free = 0         # f(i,0)
        cool = -10**18   # f(i,2)

        for p in prices:
            new_hold = max(hold, free - p)
            new_free = max(free, cool)      # rest
            new_cool = hold + p             # just sold
            hold, free, cool = new_hold, new_free, new_cool

        return(max(free, cool))
    

if __name__ == "__main__":
    # Test case
    prices = [1,2,3,0,2]
    solution = Solution2()
    result = solution.maxProfit(prices)
    print(f"Maximum profit: {result}")