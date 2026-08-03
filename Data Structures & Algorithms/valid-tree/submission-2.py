class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        map = {i: [] for i in range(n)}
        for x, y in edges:
            map[x].append(y)
            map[y].append(x)

        visited = set()
        def dfs(parent, vertex):
            if vertex in visited:
                return False

            visited.add(vertex)
            for v in map[vertex]:
                if v == parent:
                    continue
                if not dfs(vertex, v):
                    return False
            return True

        return dfs(-1, 0) and n == len(visited)