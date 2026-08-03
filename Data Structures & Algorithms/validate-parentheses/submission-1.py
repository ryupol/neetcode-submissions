class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_prts = {")": "(", "]": "[", "}": "{"}
        for c in s:
            if c in map_prts:
                if stack and stack[-1] == map_prts[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
                
            