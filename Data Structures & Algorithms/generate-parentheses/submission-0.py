class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(c):
            if len(c) > n * 2:
                return

            if self.checkFormed(c, n):
                res.append(c)
            dfs(c + "(")
            dfs(c + ")")

        dfs("")
        return res

    def checkFormed(self, s: str, n: int) -> bool:
        if len(s) != n * 2:
            return False

        stack = []
        for c in s:
            if not stack and c == ")":
                return False

            if c == "(":
                stack.append(c)
            else:
                stack.pop()

        return len(stack) == 0