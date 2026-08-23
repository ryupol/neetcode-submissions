class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        mm, nn = len(grid), len(grid[0])
        visited = [[False] * nn for _ in range(mm)]
        res = 0

        def dfs(row, col):
            if row < 0 or row >= mm or col < 0 or col >= nn:
                return
            if visited[row][col]:
                return    

            if grid[row][col] == "1":
                visited[row][col] = True  
            else:
                return 

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)


        for m in range(mm):
            for n in range(nn):
                if visited[m][n]:
                    continue

                if grid[m][n] == "0":
                    visited[m][n] == True
                    continue
                else:
                    dfs(m, n)
                    res += 1
        return res