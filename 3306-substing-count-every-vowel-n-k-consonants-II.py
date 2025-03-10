from collections import Counter

# Very Slow Solution
class SlowSolution:
    def check_vowels(self, wrd, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vowel_set = set()
        consonant_count = 0

        for char in wrd:
            if char in vowels:
                vowel_set.add(char)
            else:
                consonant_count += 1
        
        return len(vowel_set) == 5 and consonant_count == k

    def countOfSubstrings(self, word: str, k: int) -> int:
        occ = 0
        n = len(word)

        # Iterate over all starting points
        for i in range(n):
            # Iterate over all valid substring lengths (min length = 5+k)
            for j in range(i + 5 + k, n + 1):
                substr = word[i:j]
                if self.check_vowels(substr, k):
                    occ += 1

        return occ

# Hashmap and Sliding Windows -- Learn Again
class Solution:
    def is_vowel(self, char):
        """Check if a character is a vowel."""
        return char in {'a', 'e', 'i', 'o', 'u'}

    def countOfSubstrings(self, word: str, k: int) -> int:
        total_valid_substrings = 0
        vowel_set = set()  # To track unique vowels
        consonant_count = 0
        freq = Counter()  # Track character frequency
        left = 0  # Left pointer for sliding window

        for right in range(len(word)):
            # Step 1: Expand the window by adding a new character
            char = word[right]
            freq[char] += 1

            # If it's a vowel, add it to the vowel set
            if self.is_vowel(char):
                vowel_set.add(char)
            else:
                consonant_count += 1  # Otherwise, count as a consonant

            # Step 2: Shrink window if consonants exceed k
            while consonant_count > k:
                left_char = word[left]
                freq[left_char] -= 1
                
                # If left character was a vowel and it's fully removed, update the set
                if self.is_vowel(left_char) and freq[left_char] == 0:
                    vowel_set.remove(left_char)
                elif not self.is_vowel(left_char):  # If it's a consonant, decrease count
                    consonant_count -= 1
                
                left += 1  # Move left pointer forward

            # Step 3: Check if the window is valid
            if len(vowel_set) == 5 and consonant_count == k:
                total_valid_substrings += 1

        return total_valid_substrings

    
if __name__ == "__main__":
    obj = Solution()
    word = "iqeaouqi"
    k = 2
    print(obj.countOfSubstrings(word, k))