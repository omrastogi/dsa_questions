class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        for i in range(len(s)):
            substring = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in substring:
                    substring += s[j]
                    # if j == len(s)-1:
                    #     substrings.append(substring)
                else:
                    break
            substrings.append(substring)    

        max_sub = 0
        for i in substrings:
            if len(i) > max_sub:
                max_sub = len(i)
        print(substrings)
        return max_sub

# Optimised Solution
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = result = 0
        seen = {}
        for i, letter in enumerate(s):
            if seen.get(letter, -1) >= start:
                start = seen[letter] + 1
            result = max(result, i - start + 1)
            seen[letter] = i
        return result

if __name__ == "__main__":
    obj = Solution()
    ss = ["dvdf", "chwwdsadsa", "abcadfa", "bbbb", "a"]
    # ss = ["dvdf"]
    for s in ss:
        print(obj.lengthOfLongestSubstring(s))