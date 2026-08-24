class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtracking(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return

            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break

                path.append(nums[i])
                backtracking(i, path, remaining - nums[i])
                path.pop()

        backtracking(0, [], target)
        return res
