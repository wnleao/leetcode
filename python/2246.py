from collections import defaultdict

from utils import assert_solver


class Solution:

    def longestPath(self, parent: list[int], s: str) -> int:
        tree = defaultdict(list)
        for i, p in enumerate(parent):
            if i == 0:
                continue
            tree[i].append(p)
            tree[p].append(i)

        # TLE if we use lru_cache!
        cache = {}
        def dfs(parent: int, current: int) -> int:
            if parent >= 0 and s[parent] == s[current]:
                return 0

            max_child = 0
            for child in tree[current]:
                if child != parent:
                    # check cache...
                    if (current, child) not in cache:
                        cache[current, child] = dfs(current, child)

                    max_child = max(max_child, cache[current, child])

            return max_child + 1

        return max([dfs(-1, i) for i, p in enumerate(parent)])


if __name__ == '__main__':
    test_inputs = [
        ([[-1], "a"], 1),
        ([[-1,0,0,0], "aabc"], 3),
        ([[-1,0,0,1,1,2], "abacbe"], 3),
    ]
    assert_solver(Solution().longestPath, test_inputs)
