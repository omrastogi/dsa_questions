# Subproblem: dp[n] = 2*dp[n-1] + dp[n-3]
class Solution:
    def __init__(self):
        self.memo = {}
    
    def dfs(self, n):
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 1 
        if n == 1:
            return 1 
        if n == 2:
            return 2 
        
        num = 2 * self.dfs(n-1) + self.dfs(n-3) % (10**9 + 7)
        self.memo[n] = num 
        return num

    def numTilings(self, n: int) -> int:
        return self.dfs(n) % (10**9 + 7)

if __name__ == "__main__":
    obj = Solution()
    n = 3
    print(obj.numTilings(n))  # Expected: 5
    
    n = 4  
    print(obj.numTilings(n))  # Expected: 11
    
    n = 5
    print(obj.numTilings(n))  # Expected: 24