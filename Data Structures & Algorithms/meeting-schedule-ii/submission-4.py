"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for i in range(len(intervals)):
            inter = intervals[i]
            times.append((inter.start, 1))
            times.append((inter.end, -1))

        times.sort(key= lambda x: (x[0], x[1]))
        res = count = 0
        for t in times:
            count += t[1]
            res = max(res, count)
        return res