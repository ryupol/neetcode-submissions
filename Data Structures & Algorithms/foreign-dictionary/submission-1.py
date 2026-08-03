class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c: set() for w in words for c in w}

        for i in range(1, len(words)):
            w1, w2 = words[i-1], words[i]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        res = []
        visited = {} # 1 => is still in path, 0 => is visited

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = 1

            for nei in adj[c]:
                if dfs(nei):
                    return 1
            visited[c] = 0
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)

        