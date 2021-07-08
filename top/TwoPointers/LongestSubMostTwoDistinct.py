import collections


class Solution:
    def solve(self, s: str) -> int:
        dic = collections.defaultdict(int)
        counter = 0
        left, right = 0, 0
        res = 0
        while right < len(s):
            ch = s[right]
            dic[ch] += 1
            if dic[ch] == 2:
                counter += 1
            else:
                # print(l, r, r-l + 1)
                res = max(res, right - left + 1)
            right += 1
            while counter == 1:
                ch = s[left]
                dic[ch] -= 1
                if dic[ch] == 1:
                    counter -= 1
                left += 1
        return res


print(Solution().solve("pwwkew"))
