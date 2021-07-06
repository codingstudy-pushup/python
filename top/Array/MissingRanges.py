from typing import List


class Solution:

    def solve(self, nums: List[int], lower: int, upper: int) -> List[str]:
        nums = [lower - 1] + nums + [upper + 1]
        res = []

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 2:
                res.append(str(nums[i] + 1))
            elif nums[i + 1] - nums[i] > 2:
                res.append(str(nums[i] + 1) + '->' + str(nums[i + 1] - 1))

        return res

    def solve_2(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ranges=[]
        nums=[lower-1] + nums + [upper+1]
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 2:
                ranges += ['{}'.format(nums[i]+1)]
            if nums[i+1] - nums[i] > 2:
                ranges += ["{}->{}".format(nums[i]+1, nums[i+1]-1)]
        return ranges



print(Solution().solve([2,3,5,50,75], 0, 99))
print(Solution().solve_2([2,3,5,50,75], 0, 99))
