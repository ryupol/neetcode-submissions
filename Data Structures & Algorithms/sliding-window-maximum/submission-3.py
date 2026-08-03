class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        h, res = [], []

        for i, num in enumerate(nums):
            heapq.heappush(h, (-num, i)) # (num, index)
            if i + 1 < k:
                continue

            while h[0][1] <= i - k:
                heapq.heappop(h)
                
            res.append(-h[0][0])

        return res
