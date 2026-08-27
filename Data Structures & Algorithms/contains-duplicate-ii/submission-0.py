class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = defaultdict(int)

        l = 0
        for r in range(len(nums)):
            if hmap[nums[r]] == 1:
                return True

            if r - l >= k:
                hmap[nums[l]] -= 1
                l += 1
            hmap[nums[r]] += 1
        
        return False
