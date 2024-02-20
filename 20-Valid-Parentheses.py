class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for char in s:
            # print(stack)
            if stack:
                if char in pair.keys(): 
                    if stack[-1] == pair[char]:
                        stack.pop()
                        continue
            stack.append(char)            
        
        if stack: 
            return False
        else:
            return True

if __name__ == "__main__":
    obj = Solution()
    ss = ["dvdf", "chwwdsadsa", "abcadfa", "bbbb", "aa"]
    ss = ["()]"]
    for s in ss:
        print(obj.isValid(s))