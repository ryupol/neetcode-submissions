class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        window = set()
        l = 0

        for r in range(len(nums)):
            if nums[r] in window:
                return True

            if r - l >= k:
                window.remove(nums[l])
                l += 1
            window.add(nums[r])
        
        return False
