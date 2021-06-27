import collections


class Solution(object):
    def solve(self, strs):
        dic = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in dic:
                dic.get(key).append(s)
            else:
                dic[key] = [s]
        return dic.values()

    def solve_ascii(self, strs):
        # without sort, use array of 26 lowercase letters,
        # optimize to O(nk) time, and O(nk) space.
        # map the tuple of array to string.
        dic = collections.defaultdict(list)
        for s in strs:
            array = [0] * 26
            for letter in s:
                array[ord(letter) - ord('a')] += 1
            dic[tuple(array)].append(s)
        return dic.values()


print(Solution().solve(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().solve_ascii(["eat", "tea", "tan", "ate", "nat", "bat"]))
