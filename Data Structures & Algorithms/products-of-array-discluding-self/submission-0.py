class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        cum_left = []
        total = 1
        for num in nums:
            total *= num
            cum_left.append(total)

        cum_right = []
        total = 1
        for num in nums[::-1]:
            total *= num
            cum_right.append(total)

        cum_right = cum_right[::-1]

        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(cum_right[i+1])
            elif i == len(nums) - 1:
                res.append(cum_left[i-1])
            else:
                res.append(cum_right[i+1] * cum_left[i-1])
        return res
