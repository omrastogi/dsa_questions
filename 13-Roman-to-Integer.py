class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        length = len(s)
        sum = 0
        for i, char in enumerate(s):
            if i < length -1 and lookup[char] < lookup[s[i+1]]:
                    sum -= lookup[char]
            else:
                sum += lookup[char]
        
        return sum

if __name__ == "__main__":
    obj = Solution()
    ss = ["III", "IX"]
    # ss = ["dvdf"]
    for s in ss:
        print(obj.romanToInt(s))