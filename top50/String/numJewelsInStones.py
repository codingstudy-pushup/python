class Solution:

    def solve1(self, J, S):
        count = 0
        for i in J:
            count += S.count(i)
        return count

    def solve2(self, J: str, S: str) -> int:
        jSet = set(J)
        return sum(s in jSet for s in S)


if __name__ == "__main__":
    print(Solution().solve1('aA', 'aAAbbbb'))
    print(Solution().solve2('aA', 'aAAbbbb'))
