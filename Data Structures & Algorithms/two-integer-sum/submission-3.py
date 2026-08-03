class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = defaultdict(int)

        for i, num in enumerate(nums):
            cal = target - num
            if cal in hmap:
                return [hmap[cal], i]

            hmap[num] = i

        return []