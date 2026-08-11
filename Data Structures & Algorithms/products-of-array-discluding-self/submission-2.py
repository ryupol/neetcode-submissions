class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1, 1, 2, 8] first left -> right
        # [48, 24, 6, 1] second right -> left
        n = len(nums)
        left = [1] * n
        right = [1] * n
        cum = 1
        for i in range(n):
            left[i] *= cum
            cum *= nums[i]

        cum = 1
        for i in range(n - 1, -1, -1):
            right[i] *= cum
            cum *= nums[i]

        for i in range(n):
            right[i] *= left[i]

        return right