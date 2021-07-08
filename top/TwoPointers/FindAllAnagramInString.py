import collections
from typing import List


class Solution:
    def countarr(self, w):
        out = [0] * 26
        for c in w:
            out[ord(c) - ord('a')] += 1
        return out

    def solve_ord(self, s: str, p: str) -> List[int]:

        m = len(p)
        ps = self.countarr(p)
        ans = []
        ss = self.countarr(s[:m])

        if ss == ps:
            ans = [0]

        for i in range(1, len(s) - m + 1):

            left = ord(s[i - 1]) - ord('a')
            right = ord(s[i + m - 1]) - ord('a')
            ss[left] = ss[left] - 1
            ss[right] = ss[right] + 1

            if ss == ps:
                ans.append(i)
        return ans

    def solve(self, s: str, t: str) -> List[int]:
        d = collections.Counter(t)
        l, r = 0, 0
        counter = len(d)
        res = []
        while r < len(s):
            ch = s[r]
            if ch in d:
                d[ch] -= 1
                if d[ch] == 0:
                    counter -= 1
            r += 1
            while counter == 0:
                if r - l == len(t):
                    res.append(l)
                ch = s[l]
                if ch in d:
                    d[ch] += 1
                    if d[ch] > 0:
                        counter += 1
                l += 1
        return res


print(Solution().solve("bacdgabcda", "abcd"))
