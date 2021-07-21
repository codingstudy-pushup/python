from typing import List


class Solution:

    def solve1(self, s: List[str]) -> None:
        print("s", s)
        return s[::-1]

    def solve2(self, s: List[str]) -> None:
        s.reverse()
        return s

    def solve3(self, s):
        return ''.join(reversed(s))

    def solve4(self, s: List[str]) -> str:
        i , j = 0, len(s)-1
        print("s ", s)
        while i < j:
            s[i],s[j] = s[j],s[i]
            i += 1
            j -= 1
        print("22s ", s)
        return s

    def solve5(self, s: List[str]) -> None:
        for i in range(len(s) // 2):
            s[i], s[-i - 1] = s[-i - 1], s[i]
        print("solve4 ", s)


# print(Solution().solve1(["w","o","r","l","d"]))
print(Solution().solve2(["w","o","r","l","d"]))
print(Solution().solve4(["w","o","r","l","d"]))



