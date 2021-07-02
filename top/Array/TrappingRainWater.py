import collections
from typing import List


class Solution:
    def solve_1(self, height: List[int]) -> int:
        # 1 ds
        leng = len(height)
        maxLeft = [0] * leng
        maxRight = [0] * leng
        water = [0] * leng
        maxLeftVal =0
        maxRightVal = 0

        # 2
        for i in range(leng):
            maxLeftVal=max(maxLeftVal, height[i])
            maxLeft[i] =maxLeftVal

        for i in maxLeft:
            print(i, end=' ')

        for i in range(leng-1, -1, -1):
            maxRightVal = max(maxRightVal, height[i])
            maxRight[i] = maxRightVal
        print('end')
        for i in maxRight:
            print(i, end=' ')

        for i in range(leng):
            water[i]= min(maxLeft[i],maxRight[i])-height[i]
        print('end')
        return sum(water)

    def solve_2(self, height: List[int]) -> int:
        res = 0
        for i in range(1, len(height) - 1):
            maxLeft = max(height[:i])
            maxRight = max(height[i + 1:])
            print(i,'', maxLeft,'', maxRight)
            minVal = min(maxLeft, maxRight) - height[i]
            res += max(0, minVal)
        return res



print(Solution().solve_1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().solve_2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
