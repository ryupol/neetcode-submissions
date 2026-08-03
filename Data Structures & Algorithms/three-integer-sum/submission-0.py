class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)

        res = set()
        for i in range(n):
            l , r = i + 1, n - 1

            while l < r:
                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else: # total == 0
                    res.add((nums[i], nums[l], nums[r]))
                    l, r = l + 1, r - 1

        return [list(x) for x in list(res)]