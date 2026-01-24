def recursive_activity_selector(s, f, k, n):
    """
    Recursive activity selector (CLRS-style, 0-based with a dummy activity).

    Parameters
    ----------
    s : list[int]
        Start times. Assumes s[0] is a dummy with start = 0.
    f : list[int]
        Finish times. Assumes f[0] = 0 (dummy) and f is sorted non-decreasing.
    k : int
        Index of the last selected activity.
    n : int
        Total number of activities, including the dummy (len(s)).

    Returns
    -------
    set[int]
        Set of indices of selected activities (excluding dummy).
    """
    m = k + 1
    # find first activity that starts after activity k finishes
    while m < n and s[m] < f[k]:
        m += 1

    if m < n:
        # choose activity m and recurse on the rest
        return {m} | recursive_activity_selector(s, f, m, n)
    else:
        # no more compatible activities
        return set()


def activity_selector(s, f):
    """
    Wrapper that adds a dummy activity at index 0 and
    returns a sorted list of chosen activity indices.
    """
    # add dummy activity 0
    s2 = [0] + s
    f2 = [0] + f
    n = len(s2)

    chosen = recursive_activity_selector(s2, f2, 0, n)
    chosen = sorted(chosen)  # to get them in increasing index order
    chosen = [i-1 for i in chosen]
    return chosen


if __name__ == "__main__":
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    lst = activity_selector(s, f)

    print(lst)
    for i in lst:
        print(f"start: {s[i]} | finish: {f[i]}")



def activity_selection_2d_dp(s, f):
    """
    2D DP (interval DP) for unweighted activity selection.

    s, f: lists of start and finish times for n activities.
          They do NOT need to be pre-sorted; we sort by finish time inside.

    Returns:
        selected_indices: indices (in the sorted order) of chosen activities
        selected_activities: list of (start, finish) for chosen activities
        dp: the full 2D DP table dp[i][j]
    """

    n = len(s)
    activities = list(zip(s, f))

    # 1) Sort activities by finish time
    activities.sort(key=lambda x: x[1])
    s_sorted = [a[0] for a in activities]
    f_sorted = [a[1] for a in activities]

    # 2) Add two sentinel activities:
    #    a_0 with (s=0, f=0)
    #    a_{n+1} with start time > all finish times
    max_f = max(f_sorted)
    s_ext = [0] + s_sorted + [max_f + 1]
    f_ext = [0] + f_sorted + [max_f + 1]
    m = n + 2  # total including sentinels

    # 3) DP tables: dp[i][j] = max #activities in (i, j)
    dp = [[0] * m for _ in range(m)]
    choice = [[None] * m for _ in range(m)]  # to reconstruct solution

    # 4) Fill table by increasing interval size (j - i)
    for length in range(2, m):           # interval size
        for i in range(0, m - length):
            j = i + length
            best = 0
            best_k = None

            # Try all possible k between i and j
            for k in range(i + 1, j):
                # activity k must fit between i and j
                if s_ext[k] >= f_ext[i] and f_ext[k] <= s_ext[j]:
                    val = dp[i][k] + dp[k][j] + 1
                    if val > best:
                        best = val
                        best_k = k

            dp[i][j] = best
            choice[i][j] = best_k

    # 5) Reconstruct solution from interval (0, m-1)
    def build_solution(i, j):
        k = choice[i][j]
        if k is None:
            return []
        return build_solution(i, k) + [k] + build_solution(k, j)

    selected_ext = build_solution(0, m - 1)          # indices in extended arrays
    selected_sorted_indices = [k - 1 for k in selected_ext]  # back to 0..n-1
    selected_activities = [activities[i] for i in selected_sorted_indices]

    return selected_sorted_indices, selected_activities, dp

def greedy_activity_selector(s,f):
    n = len(s)
    A = [0]
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            A.append(m)
            k = m
    return A

if __name__ == "__main__":
    s = [1, 3, 0, 5, 3, 5, 6, 8, 8, 2, 12]
    f = [4, 5, 6, 7, 9, 9, 10, 11, 12, 14, 16]

    # idxs, acts, dp = greedy_activity_selector(s, f)

    # print("Selected (in sorted-by-finish order) indices:", idxs)
    # print("Selected activities (start, finish):")
    # for (st, ft) in acts:
    #     print(f"start: {st} | finish: {ft}")

    A = greedy_activity_selector(s,f)
    print(A)