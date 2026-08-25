class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        dp = [0] * (n + 1)
        dp[1], dp[2] = nums[0], nums[1]

        for j in range(3, n + 1):
            i = j - 1
            dp[j] = max(nums[i] + dp[j-2], nums[i] + dp[j-3])
        
        return max(dp[-1], dp[-2])

