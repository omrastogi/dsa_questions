class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.remove_non_alphanumeric(s)
        return self.check_palindrome(s)
        
    def check_palindrome(self, s):
        i, j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                return "false"
            i += 1
            j -= 1 
        return "true"

    def remove_non_alphanumeric(self, input_str):
        # Remove non-alphanumeric characters and convert to lowercase
        result_str = ''.join(char.lower() for char in input_str if char.isalnum())
        return result_str
    
    

if __name__ == "__main__":
    obj = Solution()
    s = "race car"
    print(obj.isPalindrome(s))