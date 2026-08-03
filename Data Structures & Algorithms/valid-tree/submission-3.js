class Solution {
    /**
     * @param {number} n
     * @param {number[][]} edges
     * @returns {boolean}
     */
    validTree(n, edges) {
        let adj = {}
        for (let i = 0; i < n; i++) {
            adj[i] = []
        }
        for (const [n1, n2] of edges) {
            adj[n1].push(n2);
            adj[n2].push(n1);
        }

        let visited = new Set()
        const dfs = (i, prev) => {
            if (visited.has(i)) return false
            visited.add(i)
            for (let j of adj[i]) {
                if (j === prev) continue
                if (!dfs(j, i)) return false
            }
            return true
        }
        return dfs(0, -1) && n === visited.size
    }
}
