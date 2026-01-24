from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        M, N = len(board), len(board[0])

        visited = set()

        def _dfs(m, n, wrd):
            if wrd == word:
                return True

            visited.add((m, n))

            for dx, dy in directions:
                nx, ny = m + dx, n + dy
                if 0 <= nx < M and 0 <= ny < N:
                    # IMPORTANT: this fixes your "in word" bug
                    # we only allow the next char to match the next position
                    if (nx, ny) not in visited and len(wrd) < len(word) and board[nx][ny] == word[len(wrd)]:
                        if _dfs(nx, ny, wrd + board[nx][ny]):
                            return True

            visited.remove((m, n))
            return False

        for i in range(M):
            for j in range(N):
                if board[i][j] == word[0]:
                    visited = set()
                    if _dfs(i, j, board[i][j]):
                        return True

        return False


if __name__ == "__main__":
    board = [
        ["A", "B", "C", "E"],
        ["S", "F", "E", "S"],
        ["A", "D", "E", "E"]
    ]
    word = "ABCEFSADEESE"

    sol = Solution()
    print(sol.exist(board, word))  # True
