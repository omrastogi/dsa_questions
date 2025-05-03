# RECURSSION
def cut_rod_recurssion(p, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, p[i-1] + cut_rod_recurssion(p, n-i))  # Fixed n-1 to n-i
    return q

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

def cut_rod_bottom_up(p, n):
    r = [0] * (n + 1)
    for j in range(1, n + 1):
        q = float('-inf')
        for i in range(1, j + 1):
            q = max(q, p[i-1] + r[j-i])
        r[j] = q
    print(r)
    return r[n]

if __name__ == "__main__":
    p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
    n = 4
    # print(cut_rod_recurssion(p, n))
    # print(cut_rod_memo(p, n, {}))
    print(cut_rod_bottom_up(p,n))

