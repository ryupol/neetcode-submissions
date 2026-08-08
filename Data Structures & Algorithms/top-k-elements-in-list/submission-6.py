class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        res = []
        for num in nums:
            hmap[num] += 1

        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in hmap.items():
            bucket[value].append(key)

        for i in range(len(bucket) - 1, -1, -1):
            if k == 0:
                return res

            if len(bucket[i]) > 0:
                for num in bucket[i]:
                    res.append(num)
                    k -= 1
        return res