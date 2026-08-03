class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mapping = {i: [] for i in range(n)}
        for x, y in edges:
            mapping[x].append(y)
            mapping[y].append(x)

        visited = set()
        def dfs(prev, curr):
            if curr in visited:
                return False
            
            visited.add(curr)
            for n in mapping[curr]:
                if n != prev and not dfs(curr, n):
                    return False
            return True
        return dfs(-1, 0) and len(visited) == n

        

            