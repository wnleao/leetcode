from collections import deque

from utils import assert_solver


class Solution:
    
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        n_sqr = n*n
        board = board[::-1]
        for r in range(n):
            if r % 2 == 1:
                board[r] = board[r][::-1]

        cells = [item for row in board for item in row]
        visited = set()
        moves = 0
        
        nodes = deque([1])
        while nodes:
            for _ in range(len(nodes)):
                curr = nodes.popleft()
                if curr == n_sqr:
                    return moves
                if curr in visited:
                    continue
                
                visited.add(curr)
                for off in range(1, 7):
                    next = curr + off
                    if next <= n_sqr:
                        nodes.append(cells[next-1] if cells[next-1] != -1 else next)
            moves += 1

        return -1


if __name__ == '__main__':
    test_inputs = [
        ([[
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,35,-1,-1,13,-1],
            [-1,-1,-1,-1,-1,-1],
            [-1,15,-1,-1,-1,-1]
        ]], 4),
        ([[
            [-1,-1],[-1,3]
        ]], 1),
    ]
    assert_solver(Solution().snakesAndLadders, test_inputs)
