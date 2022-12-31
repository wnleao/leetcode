#
# 51. N-Queens - https://leetcode.com/problems/n-queens
#
from typing import List


class Solution1:
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        
        def check_solution(solution, max_i):
            for i in range(max_i):
                if (solution[max_i] == solution[i] 
                    or solution[i] == solution[max_i] - max_i + i 
                    or solution[i] == solution[max_i] + max_i - i):
                    return False

            return True

        def dfs(solution, i):
            if i == n:
                solutions.append(solution.copy())
                return
            
            for j in range(n):
                solution[i] = j
                if check_solution(solution, i):
                    dfs(solution, i+1)
        
        dfs([0]*n, 0)

        row = '.'*n
        return [[row[:c] + 'Q' + row[c+1:] for c in sol] for sol in solutions]


class Solution2:
    
    def solveNQueens(self, n: int) -> List[List[str]]:
        diag_pos = set()
        diag_neg = set()
        cols = set()
        boards = []
        board = [['.']*n for _ in range(n)]
        def backtrack(r: int):
            if r == n:
                boards.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c in cols or r+c in diag_pos or r-c in diag_neg:
                    continue
                cols.add(c)
                diag_pos.add(r+c)
                diag_neg.add(r-c)
                board[r][c] = 'Q'
                backtrack(r+1)
                board[r][c] = '.'
                cols.discard(c)
                diag_pos.discard(r+c)
                diag_neg.discard(r-c)

        backtrack(0)

        return boards


if __name__ == "__main__":
    sol = Solution1()
    expected4 = set([''.join([".Q..","...Q","Q...","..Q."]),''.join(["..Q.","Q...","...Q",".Q.."])])
    assert expected4 == set([''.join(board) for board in  sol.solveNQueens(4)])
