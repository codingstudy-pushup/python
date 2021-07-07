import heapq
from typing import List


class Solution:
    def solve_1(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []
        for (x, y) in points:
            dist = -(x * x + y * y)
            if len(heap) == K:
                heapq.heappushpop(heap, (dist, x, y))
            else:
                heapq.heappush(heap, (dist, x, y))

        return [(x, y) for (dist, x, y) in heap]

    def solve_2(self, points: List[List[int]], K: int) -> List[List[int]]:

        heap = []
        for point in points:
            dist = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap, (-dist, point))
            if len(heap) > K:
                heapq.heappop(heap)

        return [tuple[1] for tuple in heap]

    def solve_3(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for (x, y) in points:
            d = -(x ** 2 + y ** 2)
            heapq.heappush(heap, (d, x, y))
            if len(heap) > K:
                heapq.heappop(heap)
        return [x[1:] for x in heap]


print(Solution().solve_1([[1, 3], [-2, 2]], 1))
print(Solution().solve_2([[1, 3], [-2, 2]], 1))
print(Solution().solve_3([[1, 3], [-2, 2]], 1))
