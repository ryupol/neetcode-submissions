class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges: return n

        mapping = {i: [] for i in range(n)}
        for x, y in edges:
            mapping[x].append(y)
            mapping[y].append(x)

        visited = set()
        def dfs(prev, curr):
            if curr in visited:
                return 0

            visited.add(curr)
            for n in mapping[curr]:
                if n == prev: return 0
                dfs(curr, n)
            return 1

        res = 0
        for i in range(n):
            res += dfs(i-1, i)
        return res