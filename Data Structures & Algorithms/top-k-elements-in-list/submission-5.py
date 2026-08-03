class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        max_freq = 0
        for num in nums:
            hmap[num] += 1
            max_freq = max(max_freq, hmap[num])

        freq = [[] for x in range(max_freq)]
        for num, count in hmap.items():
            freq[max_freq - count].append(num) # Store in desc order

        res = []
        for arr in freq:
            for num in arr:
                k -= 1
                res.append(num)
                if k == 0:
                    return res

        


