import collections


class Solution:
    def solve1(self, s: str) -> int:
        ch=[]
        s2 = set(s)
        print(s2)
        for i in set(s):
            if s.count(i) == 1:
                ch.append(s.index(i))
        if len(ch)>0:
            return min(ch)
        else:
            return -1

    def solve2(self, s: str) -> int:
        if not s: return -1
        d = collections.defaultdict(int)

        for char in s:
            d[char] += 1

        for i, c in enumerate(s):
            if d[c] < 2:
                return i
        return -1

    def solve3(self, s):

        from collections import Counter
        s_count = Counter(s)
        # for ch in s_count:
        #     if s_count[ch] == 1:
        #         return s.index(ch)
        for key, value in s_count.items():
            print(key, ":", value)
            if value==1 :
                return s.index(key)
        return -1

print(Solution().solve1('lovelo'))
print(Solution().solve2('lovelo'))
print(Solution().solve3('lovelo'))
