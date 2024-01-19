# Optimized for O(1) time
# Solution by https://www.youtube.com/watch?v=1ir1eryUr80
class Solution:        
    def longestPalindrome(self, s: str) -> str:
        s_prime = "#" + "#".join(s) + "#"
        radii = [0 for _ in range(len(s_prime))]
        center = 0
        right_border = 0
        max_radius = 0
        largest_palindrome_center = 0

        for i in range(len(s_prime)):
            mirror = center - (i - center)

            if i < right_border:
                if radii[mirror] < right_border - i:
                    radii[i] = radii[mirror]
                    continue
                else:
                    radii[i] = right_border - i
            
            while i - 1 - radii[i] >= 0 \
                and i + 1 + radii[i] < len(s_prime) \
                and s_prime[i - 1 - radii[i]] == s_prime[i + 1 + radii[i]]:

                radii[i] += 1

            if i + radii[i] > right_border:
                center = i
                right_border = i + radii[i]
            
            if radii[i] > max_radius:
                max_radius = radii[i]
                largest_palindrome_center = i
        start_index = (largest_palindrome_center - max_radius) // 2
        return s[start_index : start_index + max_radius]





if __name__ == "__main__":
    obj = Solution()
    ss = ["dvdf", "chwwdsadsa", "abcadfa", "bbbb", "aa"]
    # ss = ["aa"]
    for s in ss:
        print(obj.longestPalindrome(s))