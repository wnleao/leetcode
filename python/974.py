from collections import defaultdict

from utils import assert_solvers


class SolutionOnModMath:

    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        ans = 0
        rems = [0]*k
        rems[0] = 1
        prefix_sum = 0
        for num in nums:
            prefix_sum = (prefix_sum + num) % k
            ans += rems[prefix_sum]
            rems[prefix_sum] += 1

        return ans


class SolutionOn2:

    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        ans = 0
        for i in range(len(nums)):
            total = 0
            for num in nums[i:]:
                total += num
                if total%k == 0:
                    ans += 1
        return ans


if __name__ == '__main__':
    solvers = [SolutionOn2().subarraysDivByK, SolutionOnModMath().subarraysDivByK]
    test_inputs = [
        ([[4,5,0,-2,-3,1], 5], 7),
        ([[5], 9], 0)
    ]
    assert_solvers(solvers, test_inputs)
