from collections import defaultdict

from utils import assert_solver


class Solution:

    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        ans = [0]*n
        counter = defaultdict(int)
        def count(current: int, parent: int):
            start_count = counter[labels[current]]
            counter[labels[current]] += 1
            for child in tree[current]:
                if child != parent:
                    count(child, current)
            ans[current] = counter[labels[current]] - start_count

        count(0, -1)

        return ans


if __name__ == '__main__':
    test_inputs = [
        ((7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd"), [2,1,1,1,1,1,1]),
        ((4, [[0,1],[1,2],[0,3]], "bbbb"), [4,2,1,1]),
        ((5, [[0,1],[0,2],[1,3],[0,4]], "aabab"), [3,2,1,1,1])
    ]
    assert_solver(Solution().countSubTrees, test_inputs)
