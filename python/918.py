from utils import assert_solver


class Solution:
    """Based on Kadane's algorithm: https://en.wikipedia.org/wiki/Maximum_subarray_problem"""

    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        total = 0
        max_sum = min_sum = nums[0]
        curr_max_sum = curr_min_sum = 0
        for num in nums:
            total += num
            curr_max_sum += num
            curr_min_sum += num
            max_sum = max(max_sum, curr_max_sum)
            min_sum = min(min_sum, curr_min_sum)
            curr_max_sum = max(curr_max_sum, 0)
            curr_min_sum = min(curr_min_sum, 0)

        return max(max_sum, total-min_sum) if max_sum > 0 else max_sum


if __name__ == '__main__':
    test_inputs = [
        ([[-2]], -2),
        ([[2]], 2),
        ([[-2,2]], 2),
        ([[-2,-5]], -2),
        ([[1,-2,3,-2]], 3),
        ([[5,-3,5]], 10),
        ([[-3,-2,-3]], -2),
        ([[1,2,-3,-2,-3,1,2]], 6),
        ([[1,2,-5,4,-3,1,2]], 7),
    ]
    assert_solver(Solution().maxSubarraySumCircular, test_inputs)
