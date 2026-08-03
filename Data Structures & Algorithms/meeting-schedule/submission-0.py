"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1: return True

        intervals.sort(key=lambda x: x.start)
        maxSchedule = intervals[0].end
        for s in intervals[1:]:
            if s.start < maxSchedule:
                return False
            else:
                maxSchedule = s.end
        return True