from typing import List

class Solution:
    def fractionalKnapsack(self, capacity: int, values: List[int], weights: List[int]) -> float:
        # Build list of (value_per_weight, value, weight)
        items = []
        for v, w in zip(values, weights):
            ratio = v / w
            items.append((ratio, v, w))

        # Sort by ratio descending
        items.sort(key=lambda x: x[0], reverse=True)

        total_value = 0.0
        remaining = capacity

        for ratio, v, w in items:
            if remaining == 0:
                break

            if w <= remaining:
                # take whole item
                total_value += v
                remaining -= w
            else:
                # take fraction
                fraction = remaining / w
                total_value += v * fraction
                remaining = 0

        return total_value
    
from typing import List

def FRACTIONAL_KNAPSACK(v: List[int], w: List[int], W: int) -> float:
    """
    v: values of items (already sorted by v[i]/w[i] in decreasing order)
    w: weights of items (same order as v)
    W: knapsack capacity
    """
    n = len(v)

    load = 0          # (1) current weight in knapsack
    i = 0             # (2) Python index for "item i" (slide uses 1..n, here 0..n-1)
    total_value = 0.0

    # (3) while (load < W and i < n) do
    while load < W and i < n:
        wi = w[i]
        vi = v[i]

        # (4) if (wi ≤ W − load) then
        if wi <= W - load:
            # (5) take all of item i
            load = load + wi
            total_value = total_value + vi
        else:
            # (7) take (W − load) / wi of item i
            fraction = (W - load) / wi
            total_value = total_value + fraction * vi
            load = W  # knapsack is now full

        # (9) i = i + 1
        i = i + 1

    return total_value


if __name__ == "__main__":
    # Example input (you can tweak these for testing)
    capacity = 50
    values = [60, 100, 120]
    weights = [10, 20, 30]

    # sol = Solution()
    # ans = sol.fractionalKnapsack(capacity, values, weights)
    # print(ans)   # expected: 240.0 in standard textbook example

    print(FRACTIONAL_KNAPSACK(values, weights, capacity))
