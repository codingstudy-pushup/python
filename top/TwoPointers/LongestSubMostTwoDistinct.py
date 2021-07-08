import collections


class Solution:
    def solve(self, s: str) -> int:
        d = collections.defaultdict(int)
        left, right = 0, 0
        counter = 0
        res = 0

        while right < len(s):
            ch = s[right]
            d[ch] += 1
            if d[ch] == 1:
                counter += 1
            right += 1
            if counter <= 2:
                res = max(res, right - left)
            while counter > 2:
                ch = s[left]
                d[ch] -= 1
                if d[ch] == 0:
                    counter -= 1
                left += 1
        return res
print(Solution().solve("ccaabbb"))
