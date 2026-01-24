from typing import List


def cut_rod_recursive(prices: List[int], n: int) -> int:
    """
    prices[i] = price of rod of length i+1
    n = total length of rod
    return max revenue

    Implement the DP/recursion here.
    """
    if n == 0:
        return 0
    cost = float("-inf")
    for i in range(0, n):
        cost = max(cost, prices[i]+cut_rod_recursive(prices, n-i-1))
    return cost


if __name__ == "__main__":
    # quick tests (edit as you like)
    tests = [
        # (prices, n, expected)
        ([1, 5, 8, 9, 10, 17, 17, 20], 8, 22),
        ([2, 5, 7, 8], 4, 10),  # fill expected later
    ]

    for i, (prices, n, expected) in enumerate(tests, 1):
        try:
            ans = cut_rod_recursive(prices, n)
        except NotImplementedError:
            ans = "NotImplemented"

        print(f"Test {i}: prices={prices}, n={n}")
        print(f"  result   = {ans}")
        if expected is not None:
            print(f"  expected = {expected}")
        print("-" * 30)
