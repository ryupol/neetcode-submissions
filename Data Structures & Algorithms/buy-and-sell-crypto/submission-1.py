class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        res = 0
        for p in prices:
            while len(stack) > 0 and p <= stack[-1]:
                stack.pop()

            stack.append(p)
            res = max(res, stack[-1] - stack[0])

        return res