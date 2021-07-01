class Solution:
    def solve(self, S: str, K: int) -> str:
        S = S.replace('-', '')
        S = S.upper()

        for i in range(len(S) - 1 - K, -1, -K):
            S = S[:i + 1] + "-" + S[i + 1:]
        return (S)


print(Solution().solve("88F3Z-2e-9-w", 4))
print(Solution().solve("8-5g-3-J", 2))

