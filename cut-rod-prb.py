import time

# Recursive solution for the rod cutting problem
# Time Complexity: O(2^n)
# This is the most basic approach that uses recursion to try all possible cuts
def cut_rod_recurssion(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i-1] + cut_rod_recurssion(p, n-i))
    return q

# Top-down memoized solution for the rod cutting problem
# Time Complexity: O(n^2)
# Uses memoization to store previously computed results and avoid redundant calculations
def cut_rod_memo(p, n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i-1] + cut_rod_memo(p, n-i, memo))
    memo[n] = q
    return q

# Bottom-up dynamic programming solution for the rod cutting problem
# Time Complexity: O(n^2)
# Builds solution iteratively from smaller subproblems to larger ones
def cut_rod_bottom_up(p, n):
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            q = max(q, p[i-1] + r[j-i])
        r[j] = q
    print(f"Values table: {r}")
    return r[n]

if __name__ == "__main__":
    # Extended price list to length 50 by repeating pattern with some variation
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 
         32, 35, 38, 40, 42, 45, 47, 50, 52, 55,
         57, 60, 62, 65, 67, 70, 72, 75, 77, 80]
    n = 20
    
    # Test recursive solution
    start = time.time()
    result = cut_rod_recurssion(p, n)
    end = time.time()
    print(f"\nRecursive Solution:")
    print(f"Maximum value: {result}")
    print(f"Time taken: {(end - start)*1000:.4f} ms")
    
    # Test memoized solution
    start = time.time()
    result = cut_rod_memo(p, n, {})
    end = time.time()
    print(f"\nMemoized Solution:")
    print(f"Maximum value: {result}")
    print(f"Time taken: {(end - start)*1000:.4f} ms")
    
    # Test bottom-up solution
    start = time.time()
    result = cut_rod_bottom_up(p, n)
    end = time.time()
    print(f"\nBottom-up Solution:")
    print(f"Maximum value: {result}")
    print(f"Time taken: {(end - start)*1000:.4f} ms")
