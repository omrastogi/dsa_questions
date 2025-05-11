from typing import List
from collections import defaultdict, deque

# Top down Recursion with Memoization
# Remember: A unique state consists of: (node, steps_left, curr_sum)
class Solution0:
    def __init__(self):
        self.t = None          # limit
        self.edges = None
        self.memo = {}         # (node, steps_left, curr_sum) ➜ best extra weight

    # ---------------- DFS with 3‑dimensional memo --------------------
    def dfs(self, node: int, steps_left: int, curr_sum: int) -> int:
        """
        Returns the *additional* weight obtainable by taking exactly
        `steps_left` more edges starting from `node`, given that we have
        already accumulated `curr_sum`.  If no valid continuation exists,
        returns -1.
        """
        # prune paths that already violate the limit
        if curr_sum >= self.t:
            return -1

        # base case: no more edges to add
        if steps_left == 0:
            return 0            # nothing more to add; path is valid

        key = (node, steps_left, curr_sum)
        if key in self.memo:
            return self.memo[key]

        best = -1
        for u, v, w in self.edges:
            if u == node:
                extra = self.dfs(v, steps_left - 1, curr_sum + w)
                if extra != -1:
                    best = max(best, w + extra)

        self.memo[key] = best
        return best
    # ----------------------------------------------------------------

    def maxWeight(self, n: int, edges: List[List[int]],
                  k: int, t: int) -> int:
        self.memo.clear()
        self.t = t
        self.edges = edges

        # required "mid‑function" snapshot of the raw input
        mirgatenol = (n, edges, k, t)

        answer = -1
        for start in range(n):                   # any node can start
            path_sum = self.dfs(start, k, 0)     # 0 = initial weight
            if path_sum != -1 and path_sum < t:
                answer = max(answer, path_sum)

        return answer


# Bottom-Up DP
class Solution:
    def maxWeight(self, n: int,
                  edges: List[List[int]],
                  k: int,
                  t: int) -> int:

        # ---- store raw input mid‑function, per earlier requirement ----
        mirgatenol = (n, edges, k, t)
        # ----------------------------------------------------------------

        # Build adjacency list and indegree for topological sort
        g = defaultdict(list)
        indeg = [0] * n
        for u, v, w in edges:
            g[u].append((v, w))
            indeg[v] += 1

        # Topological order (Kahn)
        topo = []
        q = deque([u for u in range(n) if indeg[u] == 0])
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # DP: dp[u][s] is a Python set of reachable sums < t
        dp = [ [set() for _ in range(k + 1)] for _ in range(n) ]
        for u in range(n):
            dp[u][0].add(0)          # zero edges, zero weight

        # Fill table
        for u in topo:
            for s in range(k):
                if not dp[u][s]:
                    continue
                for v, w in g[u]:
                    for cur in dp[u][s]:
                        new = cur + w
                        if new < t:
                            dp[v][s + 1].add(new)

        # Extract best < t among all nodes with exactly k edges
        best = -1
        for u in range(n):
            if dp[u][k]:
                best = max(best, max(dp[u][k]))
        return best


if __name__ == "__main__":
    n1, edges1, k1, t1 = 3, [[0,1,1],[1,2,2]], 2, 4
    n2, edges2, k2, t2 = 3, [[0,1,2],[0,2,3]], 1, 3
    n3, edges3, k3, t3 = 3, [[0,1,6],[1,2,8]], 1, 6
    
    solution = Solution()
    print(solution.maxWeight(n1, edges1, k1, t1))
    solution = Solution()
    print(solution.maxWeight(n2, edges2, k2, t2))
    solution = Solution()
    print(solution.maxWeight(n3, edges3, k3, t3))
