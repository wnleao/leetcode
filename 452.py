class Solution:

    def findMinArrowShots(self, points: list[list[int]]) -> int:
        # xstart < xend
        points = sorted(points, key=lambda p: p[1])
        # -2**31 <= xstart < xend <= 2**31 - 1
        last_x = -2**31 - 1
        arrows = 0
        for xs, xe in points:
            if xs > last_x:
                last_x = xe
                arrows += 1

        return arrows


if __name__ == "__main__":
    sol = Solution()
    assert 2 == sol.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
    assert 4 == sol.findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])
    assert 2 == sol.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])
