class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c):
            if not (r in range(m) and c in range(n)) or grid[r][c] == "0":
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1

        return res