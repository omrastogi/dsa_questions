from collections import defaultdict
from typing import Dict

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel_freq: Dict[str, int] = defaultdict(int)
        cons_freq: Dict[str, int] = defaultdict(int)
        for char in s:
            if char in "aeiou":
                vowel_freq[char] += 1
            else:
                cons_freq[char] += 1 
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
