class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by index 0
        # [1,2] [2,3], 4,12, 4,6, , 6,9,
        # [1,2], 4,12, 5,6
        # {}

        # merge => (min0,max1) , 4,12, 
        # res # [1,3], [4,12]

        intervals.sort()

        merged = intervals[0] # [min, max]
        res = []
        for l in intervals:
            if l[0] >= merged[0] and l[0] <= merged[1]:
                merged = [min(merged[0], l[0]), max(merged[1], l[1])]
            else:
                res.append(merged)
                merged = l

        res.append(merged)

        return res