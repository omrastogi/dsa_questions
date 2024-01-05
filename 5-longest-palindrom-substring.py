class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal_len = []
        N = len(s)
        for index, l in enumerate(s):
            length = 0
            for inc in range(min(index+1, N-index)):
                # print(index, inc, index+inc, index-inc)
                if s[index+inc] == s[index-inc]: 
                    if index+inc == index-inc:
                        length += 1
                    else:
                        length += 2
                else:
                    break
            pal_len.append(length)
        print(pal_len)        
        return max(pal_len)





if __name__ == "__main__":
    obj = Solution()
    ss = ["dvdf", "chwwdsadsa", "abcadfa", "bbbb", "aa"]
    # ss = ["aa"]
    for s in ss:
        print(obj.longestPalindrome(s))