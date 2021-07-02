import collections
from typing import List


class Solution:
    def solve_1(self, height: List[int]) -> int:

        leng = len(height)
        leftMax = [0] * leng
        rightMax = [0] * leng

        Water = [0] * leng

        maxLeft = 0
        maxRight = 0

        for index in range(leng):
            maxLeft = max(maxLeft, height[index])
            leftMax[index] = maxLeft

        for index in range(leng - 1, -1, -1):
            maxRight = max(maxRight, height[index])
            rightMax[index] = maxRight

        for index in range(leng):
            Water[index] = min(leftMax[index], rightMax[index]) - height[index]

        return sum(Water)

    def solve_2(self, height: List[int]) -> int:
        ans = 0
        for i in range(1, len(height) - 1):
            maxLeft = max(height[:i])
            maxRight = max(height[i + 1:])
            potential = min(maxLeft, maxRight) - height[i]
            ans += max(0, potential)
        return ans


print(Solution().solve_1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
