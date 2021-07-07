from typing import List


class Solution:

    def solve_1(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i + 1][0] < intervals[i][1]:
                return False
        return True

    def solve_2(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[0])
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


print(Solution().solve_1([[0, 30], [5, 10], [15, 20]]))
print(Solution().solve_2([[0, 30], [5, 10], [15, 20]]))
