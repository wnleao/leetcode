from collections import defaultdict, deque

from utils import assert_solver


class Solution:

    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for i, j, price in flights:
            graph[i].append((j, price))

        visited = [float('inf')]*n
        nodes = deque([(src, 0)])
        stops = 0
        while nodes and stops <= k:
            for _ in range(len(nodes)):
                i, cost = nodes.popleft()
                for j, price in graph[i]:
                    if cost + price < visited[j]:
                        visited[j] = cost + price
                        nodes.append((j, visited[j]))
            stops += 1

        return int(visited[dst]) if visited[dst] < float('inf') else -1


if __name__ == '__main__':
    test_inputs = [
        ((4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1), 700),
        ((3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1), 200),
        ((3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0), 500),
        ((4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 0), -1),
    ]
    assert_solver(Solution().findCheapestPrice, test_inputs)
