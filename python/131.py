from utils import assert_solvers


class SolutionOptim:

    def partition(self, s: str) -> list[list[str]]:
        n = len(s)

        palindromes: list[list[bool | None]] = [[None]*n for _ in range(n)]
        def is_palindrome(i: int, j: int) -> bool | None:
            if i >= j:
                return True
            if palindromes[i][j] is None:
                palindromes[i][j] = s[i] == s[j] and is_palindrome(i+1, j-1)
            return palindromes[i][j]

        partitions = [[] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if not is_palindrome(i, j):
                    continue
                if j == n-1:
                    partitions[i].append([s[i:j+1]])
                else:
                    partitions[i] += [[s[i:j+1]] + parts for parts in partitions[j+1]]

        return partitions[0]


class SolutionRecursive:

    def partition(self, s: str) -> list[list[str]]:

        def is_palindrome(sub: str) -> bool:
            i, j = 0, len(sub)-1
            while i < j:
                if sub[i] != sub[j]:
                    return False
                i += 1
                j -= 1
            return True

        def search(sub: str) -> list[list[str]]:
            if not sub:
                return []
            ans = []
            if is_palindrome(sub):
                ans.append([sub])
            for i in range(1, len(sub)):
                part = sub[:i]
                if not is_palindrome(part):
                    continue
                ans += [[part] + parts for parts in search(sub[i:])]
            return ans

        return search(s)


if __name__ == '__main__':
    solvers = [SolutionOptim().partition, SolutionRecursive().partition]
    test_inputs = [
        (['aab'], [['a','a','b'],['aa','b']]),
        (['a'], [['a']])
    ]
    assert_solvers(solvers, test_inputs)
