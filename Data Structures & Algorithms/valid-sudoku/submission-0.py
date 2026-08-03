class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vert = defaultdict(set) # {n: set(), ...}
        squr = defaultdict(set) # {(m // 3, n // 3): set()}

        m, n = len(board), len(board[0])
        for i in range(m):

            horz = set()
            for j in range(n):
                num = board[i][j]
                if num == '.':
                    continue

                # Check valid by rows
                if num in horz:
                    return False
                horz.add(num)

                # Check valid by columns
                if num in vert[j]:
                    return False
                vert[j].add(num)

                # Check valid in squares
                block = (i // 3, j // 3)
                if num in squr[block]:
                    return False
                squr[block].add(num)

        return True

        # horz {1 2 3}
        # vert {0: {1} 1: {2} 4: {3}}
        # squr {(0, 0): {1 2}}