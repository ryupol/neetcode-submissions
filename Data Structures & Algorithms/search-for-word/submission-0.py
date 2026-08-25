class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(row, col, index):
            if (
                not (row in range(ROWS) and col in range(COLS))
                or (row, col) in visited
                or board[row][col] != word[index]
            ):
                return False

            if index == len(word) - 1:
                return True

            visited.add((row, col))
            find_word = (
                dfs(row - 1, col, index + 1)
                or dfs(row + 1, col, index + 1)
                or dfs(row, col - 1, index + 1)
                or dfs(row, col + 1, index + 1)
            )
            visited.remove((row, col))
            return find_word

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False
