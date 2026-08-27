"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# {1:1,2:1,3:1,5:0,6:-1,7:-1,4:1,8:-1,9:-1}
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        mp = defaultdict(int)
        for interval in intervals:
            mp[interval.start] += 1
            mp[interval.end] -= 1

        res, count = 0, 0
        for _, val in sorted(mp.items()):
            count += val
            res = max(res, count)
        return res
