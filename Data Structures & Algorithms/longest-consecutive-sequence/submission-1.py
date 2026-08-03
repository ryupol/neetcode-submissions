class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        res = 0
        for num in nums:
            if (num - 1) not in hset: # Find started point
            
                length = 1
                while (num + length) in hset:
                    length += 1
                res = max(res, length)
    
        return res