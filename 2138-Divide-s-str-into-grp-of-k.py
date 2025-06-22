from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        part = []
        N = len(s)
        i, j = 0, 0
        for _ in range(N):
            if j == k:
                print(i, j)
                part.append(s[i:i+j])
                j = 0 
                i += k 
            j += 1 
        if j != 0:
            part.append(s[i:j+i]+fill*(k-j))
        return part

if __name__ == "__main__":
    # Test cases
    solution = Solution()
    
    # Test case 1
    s1 = "abcdefghi"
    k1 = 3
    fill1 = "x"
    print(solution.divideString(s1, k1, fill1))  # Expected: ["abc", "def", "ghi"]
    
    # Test case 2 
    s2 = "abcdefghij"
    k2 = 3
    fill2 = "x"
    print(solution.divideString(s2, k2, fill2))  # Expected: ["abc", "def", "ghi", "jxx"]