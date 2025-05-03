# Introduction to Algorithm by Thomaas Cormen - Exercise - 15.1-5 

def fibonacci(a, b, n):
    if n == 0:
        return a
    return fibonacci(b, a+b, n-1)

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n == 0 or n == 1:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
    return memo[n]

# Test the memoized version
print("With memoization:")
print(fibonacci_memo(5))  # Will print the 5th Fibonacci number
print()
print("Original recursive version:")
print(fibonacci(1, 1, 5))  # Will print the 5th Fibonacci number
