from data_structures import UnionFind


class SolutionUnionFind:

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        uf = UnionFind(m*n)

        found_island = False
        for j in range(m):
            for i in range(n):
                if grid[j][i] == 0:
                    continue

                found_island = True
                p = j*n + i
                if i+1 < n and grid[j][i+1] == 1:
                    uf.union(p, j*n+i+1)

                if j+1 < m and grid[j+1][i] == 1:
                    uf.union(p, (j+1)*n+i)

        return max(uf.sizes) if found_island else 0


class SolutionDFS:

    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(j, i):
            grid[j][i] = 0
            return (1 + (dfs(j, i+1) if i+1  < n and grid[j][i+1] else 0) 
                      + (dfs(j, i-1) if i-1 >= 0 and grid[j][i-1] else 0) 
                      + (dfs(j+1, i) if j+1  < m and grid[j+1][i] else 0)                    
                      + (dfs(j-1, i) if j-1 >= 0 and grid[j-1][i] else 0))

        max_size = 0
        for j in range(m):
            for i in range(n):
                if grid[j][i]:
                    max_size = max(max_size, dfs(j, i))

        return max_size


if __name__ == '__main__':
    sol = SolutionDFS()
    grid = [
            [0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0],
        ]
    assert 6 == sol.maxAreaOfIsland(grid)

    grid = [[1]]
    assert 1 == sol.maxAreaOfIsland(grid)
