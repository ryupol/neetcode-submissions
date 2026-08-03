"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        if n <= 0: return 0
        
        intervals.sort(key=lambda x: x.start)
        min_day = 1
        q = [intervals[0].end]
        for i in range(1, n):
            inter = intervals[i]

            if inter.start < min(q):
                min_day += 1
                q.append(inter.end)
            else:
                q.sort()
                q.pop(0)
                q.append(inter.end)
        return min_day