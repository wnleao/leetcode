#
# 980. Unique Paths III - https://leetcode.com/problems/unique-paths-iii/
#
from typing import List


class SolutionNonRecursive:

    def __init__(self):
        self.moves = [(1,0),(-1,0),(0,1),(0,-1)]
        self.grid = []
        self.num_rows = -1
        self.num_cols = -1

    def is_cell_valid(self, r, c):
        return r >= 0 and r < self.num_rows and c >= 0 and c < self.num_cols and self.grid[r][c] != -1

    def explore(self, cr, cc, visited) -> list:
        next_moves = [(cr+r, cc+c) for r, c in self.moves]
        return [nm for nm in next_moves if self.is_cell_valid(*nm) and not nm in visited]

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.num_rows, self.num_cols = len(grid), len(grid[0])

        # find start and end square
        sr, sc = 0, 0
        ws = 0
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell == 1:
                    sr, sc = r, c
                if cell == 0:
                    ws += 1

        # start searching paths from start to goal
        # (cr, cc), visited
        up = 0
        states = [(sr, sc, set())]
        while states:            
            cr, cc, visited = states.pop()
            visited = visited.copy()
            visited.add((cr, cc))

            next_states = self.explore(cr, cc, visited)
            for nr, nc in next_states:
                if grid[nr][nc] == 2:
                    if len(visited) == ws+1:
                        up += 1
                else:
                    states.append((nr, nc, visited))

        return up


class SolutionDFSBacktrack:

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        num_rows, num_cols = len(grid), len(grid[0])

        sr, sc = 0, 0
        allowed_squares = 0
        for r, row in enumerate(self.grid):
            for c, cell in enumerate(row):
                if cell == 1:
                    sr, sc = r, c
                if cell == 0:
                    allowed_squares += 1
        
        def dfs(cr, cc, ws) -> int:
            unique_paths = 0
            for r, c in [(cr-1, cc), (cr+1, cc), (cr, cc-1), (cr, cc+1)]:
                if r < 0 or r >= num_rows or c < 0 or c >= num_cols:
                    # out of bounds
                    continue
                if grid[r][c] == 0:
                    # visit square
                    grid[r][c] = -1
                    unique_paths += dfs(r, c, ws-1)
                    # backtrack
                    grid[r][c] = 0
                elif grid[r][c] == 2:
                    unique_paths += ws == 0
            
            return unique_paths

        return dfs(sr, sc, allowed_squares)


if __name__ == "__main__":
    sol = SolutionDFSBacktrack()
    assert 2 == sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]) 
    assert 4 == sol.uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,0,2]]) 
    assert 0 == sol.uniquePathsIII([[0,1],[2,0]]) 
