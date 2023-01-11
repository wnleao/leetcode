from collections import defaultdict

from utils import assert_solver


class SolutionDFS:

    def minTime(self, n: int, edges: list[list[int]], hasApple: list[bool]) -> int:
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def dfs(current: int, parent: int) -> int:
            min_time = 0
            for child in tree[current]:
                if child == parent:
                    continue
                min_time += dfs(child, current) if child in tree else hasApple[child]*2

            if (min_time > 0 or hasApple[current]) and current != 0:
                min_time += 2

            return min_time

        return dfs(0, -1)


if __name__ == '__main__':
    test_inputs = [
        ([7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]], 8),
        ([7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,False,True,False]], 6),
    ]
    assert_solver(SolutionDFS().minTime, test_inputs)
