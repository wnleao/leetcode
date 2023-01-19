from collections import Counter, defaultdict

from utils import assert_solvers


class SolutionDefaultdict:

    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        diffs = defaultdict(int)
        for i, num in enumerate(nums):
            diffs[num - i] += 1

        total_pairs = n*(n-1)//2
        for m in diffs.values():
            total_pairs -= m*(m-1)//2

        return total_pairs


class SolutionCounter:

    def countBadPairs(self, nums: list[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        for i in range(n):
            nums[i] -= i

        good_pairs = 0
        for count in Counter(nums).values():
            if count > 1:
                good_pairs += (count-1)*count//2

        return n*(n-1)//2 - good_pairs


if __name__ == '__main__':
    solvers = [SolutionDefaultdict().countBadPairs, SolutionCounter().countBadPairs]
    test_inputs = [
        ([[4,1,3,3]], 5),
        ([[1,2,3,4,5]], 0),
        ([[5]], 0),
    ]
    assert_solvers(solvers, test_inputs)
