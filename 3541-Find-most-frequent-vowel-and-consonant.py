from collections import defaultdict

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_freq = defaultdict(int)
        cons_freq = defaultdict(int)
        for i in s:
            if i in "aeiou":
                vowel_freq[i] += 1
            else:
                cons_freq[i] += 1 
        max_vowel = max(vowel_freq.values()) if vowel_freq else 0
        max_cons = max(cons_freq.values()) if cons_freq else 0
        return max_vowel + max_cons

if __name__ == "__main__":
    s1 = "successes"
    s2 = "aeiaeia"
    s3 = "a"
    solution = Solution()
    print(solution.maxFreqSum(s1))
    print(solution.maxFreqSum(s2))
    print(solution.maxFreqSum(s3))

