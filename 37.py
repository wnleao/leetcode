#
# 37. Sudoku Solver - https://leetcode.com/problems/sudoku-solver/description/
#
from typing import List


class SolutionState:
    """Auxiliary class to keep track of the already visited values."""

    def __init__(self, board: List[List[str]]):
        n = len(board)
        # each index in self.state will keep track of the visited values according to:
        #   0: rows, 1: columns, 2: quadrants/blocks
        self.state = [[[False]*(n+1) for _ in range(n)] for _ in range(3)]
        self.empty_cells = []

         # load board initial state
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == '.':
                    self.empty_cells.append((r, c))
                else:
                    self.update(r, c, int(cell), True)
    
    def update(self, r: int, c: int, value: int, status: bool):
        self.state[0][r][value] = status
        self.state[1][c][value] = status
        self.state[2][(r//3)*3 + c//3][value] = status

    def exists(self, r: int, c: int, value: int) -> bool:
        return self.state[0][r][value] or self.state[1][c][value] or self.state[2][(r//3)*3 + c//3][value]


class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        solution_state = SolutionState(board)
        empty_cells = solution_state.empty_cells

        def backtrack(i):
            if i == -1: 
                return True

            r, c = empty_cells[i]
            for v in range(1, 10):
                if solution_state.exists(r, c, v):
                    continue
                
                board[r][c] = str(v)
                solution_state.update(r, c, v, True)
                if backtrack(i-1):
                    return True
                solution_state.update(r, c, v, False)
                board[r][c] = '.'
            
            return False

        # the board will be modified in-place
        backtrack(len(empty_cells)-1)

        return


if __name__ == "__main__":
    sol = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    expected = [
        ["5","3","4","6","7","8","9","1","2"],
        ["6","7","2","1","9","5","3","4","8"],
        ["1","9","8","3","4","2","5","6","7"],
        ["8","5","9","7","6","1","4","2","3"],
        ["4","2","6","8","5","3","7","9","1"],
        ["7","1","3","9","2","4","8","5","6"],
        ["9","6","1","5","3","7","2","8","4"],
        ["2","8","7","4","1","9","6","3","5"],
        ["3","4","5","2","8","6","1","7","9"]
    ]
    sol.solveSudoku(board)
    assert expected == board
