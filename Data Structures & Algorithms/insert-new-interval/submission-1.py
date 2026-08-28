class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            if not intervals:
                return [newInterval]

            l, r = 0, len(intervals) - 1

            while l <= r:
                mid = (l + r) // 2

                if intervals[mid][0] < newInterval[0]:
                    l = mid + 1
                elif intervals[mid][0] > newInterval[0]:
                    r = mid - 1
                else:
                    l = mid
                    break
            intervals.insert(l, newInterval)

            res = []
            min_start = intervals[0][0]
            max_end = intervals[0][1]
            for start, end in intervals:
                if start > max_end:
                    res.append([min_start, max_end])
                    min_start = start
                    max_end = end
                else:
                    max_end = max(max_end, end)
                    min_start = min(min_start, start)
            res.append([min_start, max_end])
            return res
