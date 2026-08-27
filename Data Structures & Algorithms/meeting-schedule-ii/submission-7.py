"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x.start)

        rooms = [intervals[0].end]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            min_end = rooms[0]
            if curr.start >= min_end:
                heapq.heappop(rooms)
    
            heapq.heappush(rooms, curr.end)

        return len(rooms)
