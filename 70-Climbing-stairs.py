class Solution: 
    def __init__(self):
        self.dp = {} 
    
    def climber(self, n):
        if n in self.dp:
            return self.dp[n]
        if n == 1:
            return 1
        if n == 2:
            return 2
        self.dp[n] = self.climber(n - 1) + self.climber(n - 2)
        return self.dp[n]

    def climbStairs(self, n: int) -> int:
        return self.climber(n)

# Main gate
if __name__ == "__main__":
    n = 10  # Hardcoded input
    solution = Solution()
    print(f"Number of ways to climb {n} steps: {solution.climbStairs(n)}")
