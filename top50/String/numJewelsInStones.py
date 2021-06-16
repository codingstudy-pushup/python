class Solution:
    def numJewelsInStones(self, J, S):
        Jset = set(J)
        return sum(s in Jset for s in S)


if __name__ == "__main__":
    print(Solution().numJewelsInStones('aA', 'aAAbbbb'))
