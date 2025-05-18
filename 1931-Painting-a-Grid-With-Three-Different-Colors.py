"""
Coding: 
0 --> red
1 --> green 
2 --> blue
"""
MOD = 7 + 10**9
class Solution:
    
    def recurse_rows(self, row_left, row_till_now, prev_col):
        if row_left == 0:
            return [tuple(row_till_now)]

        curr_index = len(row_till_now)
        all_rows = []

        for color in range(3):
            if row_till_now and row_till_now[-1] == color:  # vertical check
                continue
            if prev_col and prev_col[curr_index] == color:  # horizontal check
                continue
            all_rows.extend(
                self.recurse_rows(row_left - 1, row_till_now + [color], prev_col)
            )
        return all_rows

    def recurse_col(self, col_left, prev_col):
        if col_left == 0:
            return 1
        key = (col_left, tuple(prev_col))
        if key in self.memo:
            return self.memo[key]

 
        all_rows = self.recurse_rows(self.total_row, [], prev_col)
        cnt = 0
        for row in all_rows:
            cnt = (cnt + self.recurse_col(col_left - 1, row)) % MOD

        self.memo[key] = cnt
        return cnt


    def colorTheGrid(self, m: int, n: int) -> int:
        self.total_row = m 
        self.total_col = n
        self.memo = {}
        first_col = [-1] * (m+1) # buffer row
        return self.recurse_col(self.total_col, first_col)


if __name__ == "__main__":
    sol = Solution()
    # Example: m = 2, n = 3
    m = 2
    n = 3
    print(sol.colorTheGrid(m, n))  # Output the result for m=2, n=3


