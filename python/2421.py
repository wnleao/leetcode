import math
from collections import defaultdict

from data_structures import UnionFind
from utils import assert_solver


class Solution:

    def numberOfGoodPaths(self, vals: list[int], edges: list[list[int]]) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        candidates = defaultdict(list)
        for i, v in enumerate(vals):
            candidates[v].append(i)

        uf = UnionFind(len(vals))
        paths = uf.components

        # We need to add edges starting from the lowest value,
        # in that way, we guarantee that only nodes with
        # node_value <= val could be actually connected
        for val in sorted(candidates.keys()):
            for node in candidates[val]:
                for neigh in tree[node]:
                    if vals[neigh] <= val:
                        uf.union(node, neigh)

            root_count = defaultdict(int)
            for node in candidates[val]:
                root_count[uf.find(node)] += 1

            for count in root_count.values():
                # Note that a path and its reverse are counted as the same path.
                # For example, 0 -> 1 is considered to be the same as 1 -> 0.
                paths += math.comb(count, 2)

        return paths


if __name__ == '__main__':
    test_inputs = [
        ([[1,3,2,1,3], [[0,1],[0,2],[2,3],[2,4]]], 6),
        ([[1,1,2,2,3], [[0,1],[1,2],[2,3],[2,4]]], 7),
    ]
    assert_solver(Solution().numberOfGoodPaths, test_inputs)
