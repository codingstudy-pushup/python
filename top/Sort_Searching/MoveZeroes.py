from typing import List


class Solution:
    def solve_end(self, nums: List[int]) -> None:
        index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        while(index < len(nums)):
            nums[index]=0
            index +=1
        # for i in range(len(nums)):
        #     print("i ",nums[i])
        return nums


    def solve_start(self, nums: List[int]) -> None:
        index = len(nums)-1
        k = 0

        for i in range(index, -1, -1):
            if nums[i] != 0:
                nums[index] = nums[i]
                index -= 1

        while(index >= 0):
            nums[index]=0
            index -=1
        # for i in range(len(nums)):
        #     print("i ",nums[i])
        return nums

    def solve_2(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k] = nums[i]
                k += 1
        nums[k:(len(nums))] = [0] * (len(nums) - k)
        for i in range(len(nums)):
            print(nums[i], end =' ')


print(Solution().solve_start([0, 3, 2, 0, 8, 5]))
print(Solution().solve_end([0, 3, 2, 0, 8, 5]))
print(Solution().solve_2([0, 3, 2, 0, 8, 5]))
