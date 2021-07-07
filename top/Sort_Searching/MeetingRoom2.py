import heapq
from typing import List


class Solution:

    def solve_1(self, intervals):
        intervals.sort(key=lambda x: x[0])
        heap = []
        for i in intervals:
            if heap and heap[0] <= i[0]:
                # pop, push
                heapq.heapreplace(heap, i[1])
            else:
                # push
                heapq.heappush(heap, i[1])
        return len(heap)

    def solve_2(self, intervals: List[List[int]]) -> int:
        h = []
        sort = sorted(intervals)
        for i in sort:
            # need a new meeting room
            if h == [] or h[0] > i[0]:
                heapq.heappush(h, i[1])
            # don't need a new meeting room, just update the end time
            else:
                heapq.heapreplace(h, i[1])
        return len(h)

    def solve_3(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        meeting_room = [intervals[0][1]]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= meeting_room[-1]:
                meeting_room.pop()
            meeting_room.append(intervals[i][1])
            meeting_room.sort(reverse=True)
        return len(meeting_room)


print(Solution().solve_1([[0, 30], [5, 10], [15, 20]]))
print(Solution().solve_2([[0, 30], [5, 10], [15, 20]]))
