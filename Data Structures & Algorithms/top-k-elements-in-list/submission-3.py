class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = Counter(nums)
        sort_hmap = dict(sorted(hmap.items(), key=lambda x: x[1], reverse=True))

        res = []
        for num, count in sort_hmap.items():
            if k <= 0:
                break
            res.append(num)
            k -= 1

        
        return res

        


