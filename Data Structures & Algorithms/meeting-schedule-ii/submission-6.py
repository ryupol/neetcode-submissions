"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
# (1, 6) (2, 3) (3, 4) (4, 10) (6, 10) -> [6,10]
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x.start)

        rooms = [intervals[0].end]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr.start >= rooms[0]:
                heapq.heappop(rooms)
                heapq.heappush(rooms, curr.end)
            else:
                heapq.heappush(rooms, curr.end)

        return len(rooms)
