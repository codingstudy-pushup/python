from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        curMax = nums[0]
        allMax = nums[0]

        for num in nums[1:]:
            curMax = max(num, curMax + num)
            allMax = max(allMax, curMax)
        return allMax


print(Solution().solve([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
