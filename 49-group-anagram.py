from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i, s in enumerate(strs):
            hash = ''.join(sorted(s)) # Ways to hash a string for anagram
            if hash in d.keys():
                d[hash].append(s)
            else:
                d[hash] = [s]
        return list(d.values())  


if __name__ == "__main__":
    obj = Solution()
    s = ["eatt","ttea", "eat","tea","tan","ate","nat","bat"]
    print(obj.groupAnagrams(s))