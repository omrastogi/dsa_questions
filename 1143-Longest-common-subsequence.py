# DP - BottomUp (Tabulation)
class Solution0:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        # dp[i][j] = LCS length of text1[:i] and text2[:j]
        dp = [[0]*(m+1) for _ in range(n+1)]
        for row in dp:
            print(' '.join(map(str, row)))
        print()
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        for row in dp:
            print(' '.join(map(str, row)))
        print()
        return dp[n][m]

# Extra optimization with Roll over (just using the last row for updation)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1  # Always make text1 the longer one

        prev = [0] * (len(text2) + 1)
        curr = [0] * (len(text2) + 1)

        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev, curr = curr, prev  # Roll over
            # The value of old_prev is useless the memory allocation is being used. 

        return prev[-1]

if __name__ == "__main__":
    # Hardcoded test cases
    text1_cases = ["abcde", "abc", "abc", "ezupkr"]
    text2_cases = ["ace", "abc", "def", "ubmrapg"]
    
    obj = Solution()
    for t1, t2 in zip(text1_cases, text2_cases):
        result = obj.longestCommonSubsequence(t1, t2)
        print(f"text1: {t1}, text2: {t2}")
        print(f"Longest common subsequence length: {result}\n")