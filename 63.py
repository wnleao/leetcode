#
# 63. Unique Paths II - https://leetcode.com/problems/unique-paths-ii
#
from typing import List


class SolutionSimpleDP:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[-1][-1] == 1:
            return 0

        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[-2][-2] = 1
        for j in range(m-1, -1, -1):
            for i in range(n-1, -1, -1):
                if obstacleGrid[j][i] == 1:
                    dp[j][i] = 0
                elif i != n-1 or j != m-1:
                    dp[j][i] = dp[j+1][i] + dp[j][i+1] 


        return dp[0][0]


class SolutionReuseGrid:

    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        if grid[m-1][n-1] == 1:
            return 0

        # Now the cell value means that we can reach that cell with 
        # a given number of valid paths
        grid[m-1][n-1] = 1
        for j in range(m-2, -1, -1):
            grid[j][n-1] = grid[j+1][n-1] if grid[j][n-1] == 0 else 0
        for i in range(n-2, -1, -1):
            grid[m-1][i] = grid[m-1][i+1] if grid[m-1][i] == 0 else 0

        for j in range(m-2, -1, -1):
            for i in range(n-2, -1, -1):
                if grid[j][i] == 0:
                    grid[j][i] = grid[j+1][i] + grid[j][i+1]
                else:
                    grid[j][i] = 0

        return grid[0][0]


if __name__ == "__main__":
    solvers = [SolutionSimpleDP(), SolutionReuseGrid()]
    test_inputs = [
        ([[0,0,0],[0,1,0],[0,0,0]], 2),
        ([[0,1],[0,0]], 1),
        ([[0,0],[0,1]], 0),
        ([[0,0,0],[0,0,1],[0,1,0]], 0)
    ]
    for solver in solvers:
        for input, expected in test_inputs:
            assert solver.uniquePathsWithObstacles(input) == expected
