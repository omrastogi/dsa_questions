from typing import List 

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Create a list with n+1 elements, all initialized to 0
        result = [0] * (n + 1)
        # Loop through each number from 1 to n
        for i in range(1, n + 1):
            # For each number, count the number of 1 bits
            # by shifting the bits to the right and adding the last bit
            result[i] = result[i >> 1] + (i & 1)
        # Return the list of counts
        return result

if __name__ == "__main__":
    # Create an instance of the Solution class
    sol = Solution()
    # Hardcoded input value of 5
    n = 5
    # Call the countBits function and store the result
    result = sol.countBits(n)
    # Print the result in a formatted string
    print(f"Number of 1 bits in numbers from 0 to {n}: {result}")
