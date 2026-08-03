class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [70 30 21 20 40 80]
        # temp (40 4)
        # count 1
        # [(70 0) (30 1) (21 2 ) (20 3 0) (40 4 )]

        stack = []
        res = [0] * len(temperatures)
        for i, num in enumerate(temperatures):
            while stack and num > stack[-1][0]:
                numS, indexS = stack.pop()
                res[indexS] = i - indexS

            stack.append([num, i])
        return res
            