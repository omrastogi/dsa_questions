# DSA Microtemplates (Python)

Goal: paste a skeleton fast, then fill in problem-specific parts.

---

## DFS (recursive)

```python
def dfs(u):
    seen.add(u)
    for v in adj[u]:
        if v not in seen:
            dfs(v)

seen = set()
dfs(start)
```

## DFS (iterative)

```python
seen = {start}
stack = [start]

while stack:
    u = stack.pop()
    for v in adj[u]:
        if v not in seen:
            seen.add(v)
            stack.append(v)
```

## BFS

```python
from collections import deque

q = deque([start])
seen = {start}

while q:
    u = q.popleft()
    for v in adj[u]:
        if v not in seen:
            seen.add(v)
            q.append(v)
```

## Two pointers

### Opposite ends

```python
l, r = 0, n - 1
while l < r:
    if ok(l, r):
        l += 1
        r -= 1
    elif need_left():
        l += 1
    else:
        r -= 1
```

### Fast / slow

```python
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

## Sliding window

### Fixed size k

```python
l = 0
for r in range(n):
    add(nums[r])
    if r - l + 1 > k:
        remove(nums[l])
        l += 1
    if r - l + 1 == k:
        update_answer(l, r)
```

### Variable size (shrink while invalid)

```python
l = 0
for r in range(n):
    add(nums[r])
    while invalid():
        remove(nums[l])
        l += 1
    update_answer(l, r)  # window [l..r] is valid
```

## Binary search

### Exact match

```python
l, r = 0, n - 1
while l <= r:
    m = (l + r) // 2
    if a[m] == x:
        return m
    if a[m] < x:
        l = m + 1
    else:
        r = m - 1
return -1
```

### Lower bound (first i with a[i] >= x)

```python
l, r = 0, n  # [l, r)
while l < r:
    m = (l + r) // 2
    if a[m] < x:
        l = m + 1
    else:
        r = m
return l
```

### Upper bound (first i with a[i] > x)

```python
l, r = 0, n  # [l, r)
while l < r:
    m = (l + r) // 2
    if a[m] <= x:
        l = m + 1
    else:
        r = m
return l
```

### Binary search on answer (min feasible)

```python
l, r = lo, hi
while l < r:
    m = (l + r) // 2
    if feasible(m):
        r = m
    else:
        l = m + 1
return l
```

## Monotonic stack

### Next greater to the right (store indices)

```python
st = []
ans = [-1] * n

for i in range(n):
    while st and a[st[-1]] < a[i]:
        ans[st.pop()] = i
    st.append(i)
```

### Previous smaller to the left (store indices)

```python
st = []
prev = [-1] * n

for i in range(n):
    while st and a[st[-1]] >= a[i]:
        st.pop()
    prev[i] = st[-1] if st else -1
    st.append(i)
```

## Heap

### Top-k largest (min-heap size k)

```python
import heapq

h = []
for x in nums:
    if len(h) < k:
        heapq.heappush(h, x)
    elif x > h[0]:
        heapq.heapreplace(h, x)
# h contains top-k
```

### K-way merge (k sorted lists)

```python
import heapq

h = []
for li, arr in enumerate(lists):
    if arr:
        heapq.heappush(h, (arr[0], li, 0))

out = []
while h:
    val, li, ei = heapq.heappop(h)
    out.append(val)
    ni = ei + 1
    if ni < len(lists[li]):
        heapq.heappush(h, (lists[li][ni], li, ni))
```

## Union-Find (DSU)

```python
class DSU:
    def __init__(self, n):
        self.p = list(range(n))
        self.r = [0] * n  # rank (or size)

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.r[ra] < self.r[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.r[ra] == self.r[rb]:
            self.r[ra] += 1
        return True
```

## DP patterns

### 1D DP

```python
dp = [0] * (n + 1)
dp[0] = base

for i in range(1, n + 1):
    dp[i] = transition(dp, i)
return dp[n]
```

### 2D DP

```python
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = base

for i in range(n + 1):
    for j in range(m + 1):
        dp[i][j] = transition(dp, i, j)
return dp[n][m]
```

### LIS (O(n^2))

```python
dp = [1] * n
for i in range(n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
return max(dp)
```

### LIS patience (O(n log n))

```python
def lower_bound(arr, x):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if arr[m] < x:
            l = m + 1
        else:
            r = m
    return l

tails = []
for x in a:
    i = lower_bound(tails, x)
    if i == len(tails):
        tails.append(x)
    else:
        tails[i] = x
return len(tails)
```
