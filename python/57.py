from utils import assert_solver


class Solution:

    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        if not intervals or newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        if newInterval[0] > intervals[-1][1]:
            return  intervals + [newInterval]

        def binary_search(target: int):
            i, j = 0, len(intervals)-1
            while i <= j:
                m = (i+j)//2
                if intervals[m][1] == target:
                    i = m
                    break
                elif target < intervals[m][1]:
                    j = m-1
                else:
                    i = m+1
            return i

        # search start and end of intervals
        left, right = binary_search(newInterval[0]), binary_search(newInterval[1])

        # merge intervals from left to right
        ans = intervals[:left]
        ns, ne = min(intervals[left][0], newInterval[0]), newInterval[1]
        if right < len(intervals) and ne >= intervals[right][0]:
            ne = max(ne, intervals[right][1])
            right += 1
        ans.append([ns, ne])

        return ans + intervals[right:]


if __name__ == '__main__':
    test_inputs = [
        ([[], [2,5]], [[2,5]]),
        ([[[1,3], [6,9]], [2,5]], [[1,5], [6,9]]),
        ([[[1,2], [3,5], [6,7], [8,10], [12,16]], [4,8]], [[1,2], [3,10], [12,16]]),
    ]
    assert_solver(Solution().insert, test_inputs)
