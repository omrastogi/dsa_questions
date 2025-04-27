# Essential Python Libraries for DSA

| Library     | What it's for                          | Important functions you’ll use |
|-------------|-----------------------------------------|---------------------------------|
| **collections** | Specialized data structures | `deque`, `Counter`, `defaultdict`, `OrderedDict` |
| **heapq**        | Priority Queues (Min Heap)         | `heappush`, `heappop`, `heapify` |
| **bisect**       | Binary Search Utilities            | `bisect_left`, `bisect_right`, `insort` |
| **math**         | Basic math utilities               | `gcd`, `sqrt`, `ceil`, `floor`, `log2` |
| **itertools**    | Combinatorics and Iteration Tricks | `combinations`, `permutations`, `product`, `accumulate` |
| **functools**    | Function utilities                 | `lru_cache` (for memoization) |

# Optional (only sometimes needed)

| Library     | Usecase |
|-------------|---------|
| **string**  | Easy access to alphabets, ascii letters |
| **random**  | For randomized algorithms |
| **sys**     | For fast input (`sys.stdin.readline`) when needed in contests |


# 6 Core Libraries to Remember:

collections, heapq, bisect, math, itertools, functools

# 1-Line Usage Tips for Each DSA Library

- **collections** : Use when you need fast counting, grouping, or double-ended queue (stack + queue both).
- **heapq** : Use when you need dynamic min/max retrieval (priority queue behavior).
- **bisect** : Use when you need to find insert positions quickly in sorted lists (binary search).
- **math** : Use when exact mathematical operations (gcd, sqrt, logs) are needed.
- **itertools** : Use when you need to generate combinations, permutations, or accumulated results without loops.
- **functools** : Use when you want memoization (caching results) for recursive problems (especially in DP).
- **string** : Use when you need alphabets (like 'a' to 'z') or ascii-related constants quickly.
- **random** : Use for randomized algorithms or shuffling arrays (e.g., quicksort random pivot).
- **sys** : Use for faster input/output handling in competitive programming.
