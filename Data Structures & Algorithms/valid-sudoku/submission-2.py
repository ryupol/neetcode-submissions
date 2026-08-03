class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                block = (r // 3, c // 3)
                if num == '.':
                    continue

                # Check valid
                if ( (num in rows[r]) or (num in cols[c] ) or (num in squares[block]) ):
                    return False

                rows[r].add(num)
                cols[c].add(num)
                squares[block].add(num)

        return True