class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h, res = [], []

        l = 0
        for r, num in enumerate(nums):
            heapq.heappush(h, (num * -1, r)) # (num, index)
            if r - l + 1 < k:
                continue

            hnum, hi = h[0]
            while not (l <= hi <= r):
                heapq.heappop(h)
                hnum, hi = h[0]

            res.append(hnum * -1)
            l += 1

        return res
