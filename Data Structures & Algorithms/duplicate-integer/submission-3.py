class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        maps = defaultdict(int)
        for n in nums:
            maps[n] += 1
            if maps[n] > 1:
                return True
        return False