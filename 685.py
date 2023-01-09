class Solution:

     def findRedundantDirectedConnection(self, edges: list[list[int]]) -> list[int]:
        # Simple UnionFind without path-compression
        roots = list(range(len(edges)+1))

        def find(u: int) -> int:
            root = u
            while root != roots[root]:
                root = roots[root]
            return root

        redundant = []
        selected_edge = None
        has_cycle = False
        for u, v in edges:
            root_u, root_v = find(u), find(v)
            if root_u != root_v and root_v == v:
                # directed edge
                roots[v] = u
                continue

            if root_u == root_v:
                # found cycle
                if selected_edge:
                    # a node has two parents and we found a cycle
                    # containing this edge, so this is the redundant one!
                    return selected_edge
                has_cycle = True
                redundant = [u, v]
            elif root_v != v:
                # v already has a parent!
                # keep track of which edge we are using...
                selected_edge = [roots[v], v]
                if has_cycle:
                    # If we already have a cycle, than this is the edge!
                    return selected_edge
                else:
                    # keep track of the other edge in case we don't find a cycle,
                    # then this edge would have caused the cycle
                    redundant = [u, v]

        return redundant


if __name__ == '__main__':
    sol = Solution()
    assert [2,3] == sol.findRedundantDirectedConnection([[1,2],[1,3],[2,3]])
    assert [4,1] == sol.findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]])
