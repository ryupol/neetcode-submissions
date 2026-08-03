class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # set {2, 19, 20 , 4, 10, 3, 4, 5}

        hset = set(nums)
        visited = set()
        res = 0
        for num in nums:
            count = 1
            if num in visited:
                continue
            
            while num + 1 in hset:
                visited.add(num)
                count += 1
                num += 1
            res = max(res, count)
        return res