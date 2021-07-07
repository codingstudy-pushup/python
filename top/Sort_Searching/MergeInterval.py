import heapq
from typing import List


class Solution:
    def merge(self, intervals):
        intervals.sort()
        last_merged_idx = 0
        for intv_idx in range(1, len(intervals)):
            if intervals[last_merged_idx][1] >= intervals[intv_idx][0]:
                intervals[last_merged_idx][1] = max(intervals[last_merged_idx][1], intervals[intv_idx][1])
            else:
                last_merged_idx += 1
                intervals[last_merged_idx] = intervals[intv_idx]
        return intervals[:last_merged_idx + 1]

    def solve_1(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for i in intervals:

            if not merged or merged[-1][-1] < i[0]:
                merged.append(i)

            else:
                merged[-1][-1] = max(merged[-1][-1], i[-1])
        return merged

print(Solution().solve_1([[1,3],[2,6],[8,10],[15,18]]))
