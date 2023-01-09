from data_structures import UnionFind


class Solution:

    def findRedundantConnection(self, edges: list[list[int]]) -> list[int] | None:
        ds = UnionFind(len(edges))

        ans = None
        for p, q in edges:
            if not ds.union(p-1, q-1):
                ans = [p, q]

        return ans


if __name__ == '__main__':
    sol = Solution()
    assert [2,3] == sol.findRedundantConnection([[1,2],[1,3],[2,3]])
    assert [1,4] == sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]])
