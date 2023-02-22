import math

from utils import assert_solver


class Solution:

    def shipWithinDays(self, weights: list[int], days: int) -> int:

        def check_partition(capacity: int) -> bool:
            sum_weight = 0
            sum_days = 1
            for weight in weights:
                sum_weight += weight
                if sum_weight > capacity:
                    sum_days += 1
                    sum_weight = weight

            return sum_days <= days

        i = max(weights)
        j = math.ceil(len(weights)/days)*i
        while i <= j:
            w = (i + j)//2
            if check_partition(w):
                j = w - 1
            else:
                i = w + 1

        return i


if __name__ == '__main__':
    test_inputs = [
        ([[1,2,3,4,5,6,7,8,9,10], 5], 15),
        ([[3,2,2,4,1,4], 3], 6),
        ([[1,2,3,1,1], 4], 3),
    ]
    assert_solver(Solution().shipWithinDays, test_inputs)
