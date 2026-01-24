def dfs(node, adj):
    visited = set()

    def mark_visit(u):
        visited.add(u)
        print(u)

    def _dfs(u):
        mark_visit(u)
        for v in adj[u]:
            if v not in visited:
                _dfs(v)

    _dfs(node)
    return visited


if __name__=="__main__":
    from collections import defaultdict

    n = 5  # number of nodes (0..n-1)
    edges = [(0, 1), (0, 2), (1, 3), (3, 4)]

    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)   # undirected

    print(dfs(0, adj))