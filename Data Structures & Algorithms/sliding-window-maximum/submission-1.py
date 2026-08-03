class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        # O(k * n) # Space O(1)

        res = []

        l = 0
        for r in range(k - 1, len(nums)):
            max_num = max(nums[l:r+1])
            res.append(max_num)
            l += 1

        return res
