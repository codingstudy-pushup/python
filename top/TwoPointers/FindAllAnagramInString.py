import collections
from typing import List, Counter


class Solution:
    def solve_1(self, s: str, p: str) -> List[int]:
        res = []
        if len(s) < len(p):
            return res
        pPat = [0] * 26
        sPat = [0] * 26

        for i in range(0, len(p)):
            pPat[ord(p[i]) - ord("a")] += 1
            sPat[ord(s[i]) - ord("a")] += 1
        if pPat == sPat:
            res.append(0)
        for i in range(1, len(s) - len(p) + 1):
            print('i', i)
            sPat[ord(s[i - 1]) - ord("a")] -= 1
            sPat[ord(s[i + len(p) - 1]) - ord("a")] += 1
            if pPat == sPat:
                res.append(i)
        return res

    def solve_2(self, s: str, p: str) -> List[int]:
        def makeMap(string):  # O(26)
            bitmap = [0 for i in range(26)]
            for c in string:
                bitmap[ord(c) - ord('a')] += 1
            return bitmap

        pLength = len(p)
        pPat = makeMap(p)
        sPat = makeMap(s[:pLength])
        res = []
        if sPat == sPat:
            res.append(0)

        for i in range(1, len(s) - pLength + 1):
            sPat[ord(s[i - 1]) - ord('a')] -= 1
            sPat[ord(s[i + pLength - 1]) - ord('a')] += 1
            if sPat == pPat:
                res.append(i)
        return res

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
