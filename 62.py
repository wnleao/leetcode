#
# 62. Unique Paths - https://leetcode.com/problems/unique-paths/description/
#
class Solution1:

    def uniquePaths(self, m: int, n: int) -> int:
        from functools import lru_cache
        @lru_cache
        def explore(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            
            ans = 0
            if r < m: 
                ans += explore(r+1, c)
            if c < n: 
                ans += explore(r, c+1)

            return ans

        return explore(0, 0)


class Solution2:

    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1]*n for _ in range(m)]
        
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                grid[r][c] = grid[r+1][c] + grid[r][c+1]
        
        return grid[0][0]


class Solution3:

    def uniquePaths(self, m: int, n: int) -> int:
        row = [1]*n
        
        for _ in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):
                row[c] += row[c+1]
        
        return row[0]


if __name__ == "__main__":
    sol = Solution1()
    assert 3 == sol.uniquePaths(3, 2)
    assert 28 == sol.uniquePaths(3, 7)
