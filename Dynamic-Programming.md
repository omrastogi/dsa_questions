# 🧠 Types of Dynamic Programming (DP)

Dynamic Programming problems can be solved using three main approaches:

---

## 📌 1. Top-Down DP (Memoization)

- **Concept:** Solve recursively and store results of subproblems.
- **Technique:** Recursion + `dict` (hash map) or `@lru_cache`
- **Best for:** Problems with overlapping subproblems where recursion is natural.

#### ✅ Example:
```python
memo = {}
def fib(n):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```

---

## 📌 2. Bottom-Up DP (Tabulation)

- **Concept:** Start with base cases and build up using iteration.
- **Technique:** Use a table (1D or 2D list) to track subproblem results.
- **Best for:** Performance-sensitive problems where recursion isn't ideal.

#### ✅ Example:
```python
def fib(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

---

## 📌 3. Space-Optimized DP

- **Concept:** Only keep the last few results needed instead of the full table.
- **Technique:** Use constant variables to track minimal state.
- **Best for:** Problems like Fibonacci where only the last 2 states matter.

#### ✅ Example:
```python
def fib(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

---

## 📊 Comparison Table

| Type                 | Style      | Memory      | Speed     | Notes                                  |
|----------------------|------------|-------------|-----------|----------------------------------------|
| **Top-Down (Memoized)** | Recursive  | High         | Moderate  | Elegant, but has recursion overhead    |
| **Bottom-Up (Tabular)** | Iterative  | Moderate     | Fast      | Very fast and cache-friendly           |
| **Space-Optimized**     | Iterative  | Very Low     | Fastest   | Only works when minimal state is needed |

---

> ✅ Use **Top-Down DP** when recursion feels natural.  
> ✅ Use **Bottom-Up DP** when performance matters.  
> ✅ Use **Space Optimization** when memory is tight or unnecessary to store everything.


––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# DP, Chapter-15 of Introduction to Algorithm (by Thomas Cormen)  

> The Cut-Rod Problem ([code](The-cut-rod-prb.py)) 

> Exercise 15.1-5: Fibonacci Problem ([code](febonacci-prb.py))