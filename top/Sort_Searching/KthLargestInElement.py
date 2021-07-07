from heapq import heapify, heappop
from typing import List


class Solution:
    def solve_1(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k - 1]

    def solve_2(self, nums: List[int], k: int) -> int:
        heapify(nums)

        while len(nums) > k:
            heappop(nums)
        return nums[k-2]

    def solve_3(self, nums: List[int], k: int) -> int:
        size = len(nums)
        left, right = 0, size - 1
        while True:
            cur_index = self.partition(nums, left, right)
            if cur_index > k - 1:
                right = cur_index - 1
            elif cur_index < k - 1:
                left = cur_index + 1
            else:
                return nums[cur_index]
        return nums[0]

    def partition(self, nums, left, right):
        pivot = nums[left]
        l, r = left + 1, right
        while l <= r:
            if nums[l] < pivot and nums[r] > pivot:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1
            if nums[l] >= pivot:
                l += 1
            if nums[r] <= pivot:
                r -= 1
        nums[left], nums[r] = nums[r], nums[left]
        return r


print(Solution().solve_1([2, 3, 1, 5, 6, 4], 2))
print(Solution().solve_2([2, 3, 1, 5, 6, 4], 2))
print(Solution().solve_3([2, 3, 1, 5, 6, 4], 2))
