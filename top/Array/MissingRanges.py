from typing import List


class Solution:
    def solve(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ranges=[]
        nums=[lower-1] + nums + [upper+1]
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                ranges += ["{}".format(nums[i]+1)]
            if nums[i+1] - nums[i] > 2:
                ranges += ["{}->{}".format(nums[i]+1, nums[i+1]-1)]
        return ranges

print(Solution().solve([2,3,5,50,75], 0, 99))
