import heapq
from typing import List

class Solution:
    def solve_1(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        for interval in sorted(intervals):
            if res and interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res



print(Solution().solve_1([[1,3],[2,6],[8,10],[15,18]]))
