class Solution:
    # for문 이용
    def solve_1(self, nums, target):
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                temp = nums[i] + nums[j]
                if temp == target:
                    return [i, j]
    # 리스트이용
    def solve_2(self, nums, target):
        list = []
        for i in range(len(nums)):
            if nums[i] in list:
                return [list.index(nums[i]), i]
            list.append(target - nums[i])
    # dic
    def solve_dic1(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            dic[target - nums[i]] = i

    # dic2
    def solve_dic2(self, nums, target):
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], i]
            dic[num] = i

if __name__=="__main__":
    print(Solution().solve_1([2, 8, 11, 14], 16))
    print(Solution().solve_2([2, 8, 11, 14], 16))
    print(Solution().solve_dic1([2, 8, 11, 14], 16))
    print(Solution().solve_dic2([2, 8, 11, 14], 16))
