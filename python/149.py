
import math
from collections import Counter


class SolutionOn3:
    """O(n^3) solution that uses two points as reference."""

    def maxPoints(self, points: list[list[int]]) -> int:
        N = len(points)
        if N <= 2:
            return N

        max_points = 0
        
        for i, (xi, yi) in enumerate(points[:-2]):
            for j, (xj, yj) in enumerate(points[i+1:-1]):
                num_points = 2
                slope = (yj - yi)/(xj - xi) if xj != xi else math.inf
                for (xk, yk) in points[i+j+2:]:
                    if math.isclose((yk - yi)/(xk - xi) if xk != xi else math.inf, slope):
                        num_points += 1                    
                
                max_points = max(max_points, num_points)

        return max_points


class SolutionOn2:
    """O(n^2) solution that keeps track of all possible slopes given a starting point."""

    def maxPoints(self, points: list[list[int]]) -> int:
        N = len(points)
        if N <= 2:
            return N

        max_points = 0
        for i, (xi, yi) in enumerate(points[:-1]):
            slopes = {}
            for (xj, yj) in points[i+1:]:
                slope = round((yj - yi)/(xj - xi), 9) if xj != xi else math.inf
                slopes[slope] = slopes.get(slope, 1) + 1
                max_points = max(max_points, slopes[slope])

        return max_points


class SolutionOn2UsingCounter:
    """O(n^2) solution that keeps track of all possible slopes given a starting point using Counter."""

    def maxPoints(self, points: list[list[int]]) -> int:
        N = len(points)
        if N <= 2:
            return N

        def slope(p1, p2):
            return round((p1[1] - p2[1])/(p1[0] - p2[0]), 9) if p1[0] != p2[0] else math.inf

        # +1 because we need to keep track of the starting point!
        return 1 + max([max(Counter([slope(p1, p2) for p2 in points[i+1:]]).values()) for i, p1 in enumerate(points[:-1])])


if __name__ == '__main__':
    solvers = [SolutionOn3(), SolutionOn2(), SolutionOn2UsingCounter()]
    test_inputs = [
        ([[[0,0]]], 1),
        ([[[0,0], [2,3]]], 2),
        ([[[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]], 4),
        ([[[1,1],[2,2],[3,3]]], 3),
        ([[[1,1],[2,2],[3,1],[2,3],[4,1]]], 3),
        ([[[0,0],[4,5],[7,8],[8,9],[5,6],[3,4],[1,1]]], 5),
    ]
    for solver in solvers:
        for input, expected in test_inputs:
            actual = solver.maxPoints(*input)
            assert actual == expected, f'the result for {input} was {actual} but the expected is {expected}'
