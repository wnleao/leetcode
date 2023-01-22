from functools import cache

from utils import assert_solvers


class Solution:

    def minCut(self, s: str) -> int:
        n = len(s)
        palindromes: list[list[bool | None]] = [[None]*n for _ in range(n)]
        def is_palindrome(i: int, j: int) -> bool | None:
            if i >= j:
                return True
            if palindromes[i][j] is None:
                palindromes[i][j] = s[i] == s[j] and is_palindrome(i+1, j-1)
            return palindromes[i][j]

        @cache
        def dp(i: int) -> int:
            if i >= n:
                return 0
            min_cut = n
            for j in range(i, n):
                if is_palindrome(i, j):
                    min_cut = min(min_cut, dp(j+1))
            return min_cut+1

        return dp(0)-1


if __name__ == '__main__':
    solvers = [Solution().minCut]
    test_inputs = [
        (['aab'], 1),
        (['a'], 0),
        (['ab'], 1)
    ]
    assert_solvers(solvers, test_inputs)
