class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for p in s:
            if len(stack) > 0 and (
                ( stack[-1] == "(" and p == ")") or
                ( stack[-1] == "[" and p == "]") or
                ( stack[-1] == "{" and p == "}")
                ):
                    stack.pop()
            else:
                stack.append(p)

        return True if len(stack) == 0 else False