class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hmap = defaultdict(list)
        for init, require in prerequisites:
            hmap[init].append(require)

        visited = set()
        proved = set()

        def dfs(course):
            if course in visited:
                return False

            if course not in hmap or course in proved:
                return True

            visited.add(course)
            for pre in hmap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            proved.add(course)
            return True
                
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

            