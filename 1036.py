#
# 1036. Escape a Large Maze - https://leetcode.com/problems/escape-a-large-maze
#
from typing import List
from heapq import heappop, heappush
from collections import deque


class SolutionMinHeapWithManhattanDistance:
    """Uses manhattan distance as a heuristic to explore the state space."""

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True

        blocked_set = set([tuple(p) for p in blocked])
        if tuple(source) in blocked_set or tuple(target) in blocked_set:
            return False

        max_distance = len(blocked)

        def manhattan(xa, ya, xb, yb):
            return abs(xa-xb) + abs(ya-yb)
        
        def search(start, goal):
            sx, sy = start
            gx, gy = goal
            visited = set()
            space = [(0, tuple(start))]
            while space:
                _, (cx, cy) = heappop(space)
                if manhattan(cx, cy, sx, sy) > max_distance:
                    break

                for nx, ny in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]:
                    if nx < 0 or nx >= 1_000_000 or ny < 0 or ny >= 1_000_000 or (nx, ny) in visited or (nx, ny) in blocked_set:
                        continue
                    if nx == gx and ny == gy:
                        return True
                    
                    heappush(space, (manhattan(nx, ny, gx, gy), (nx, ny)))
                    visited.add((nx, ny))

            return len(space) > 0

        return search(source, target) and search(target, source)


class SolutionSimpleBFS:

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True

        blocked_set = set([tuple(p) for p in blocked])
        if tuple(source) in blocked_set or tuple(target) in blocked_set:
            return False

        max_distance = len(blocked)
        def bfs(start, goal):
            gx, gy = goal
            visited = set()
            space = deque([tuple(start)])
            level = 0
            while space and level <= max_distance:
                length = len(space)
                for _ in range(length):
                    cx, cy = space.popleft()
                    for nx, ny in [(cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)]:
                        if nx < 0 or nx >= 1_000_000 or ny < 0 or ny >= 1_000_000 or (nx, ny) in visited or (nx, ny) in blocked_set:
                            continue
                        if nx == gx and ny == gy:
                            return True
                        
                        space.append((nx, ny))
                        visited.add((nx, ny))
                
                level += 1

            return len(space) > 0

        return bfs(source, target) and bfs(target, source)


if __name__ == "__main__":
    solvers = [SolutionSimpleBFS(), SolutionMinHeapWithManhattanDistance()]
    test_inputs = [
        (([[0,1],[1,0]], [0,0], [0,2]), False),
        (([], [0,0], [999999, 999999]), True)
    ]
    for solver in solvers:
        for input, expected in test_inputs:
            assert solver.isEscapePossible(*input) == expected
