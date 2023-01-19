from utils import assert_solver


class Solution:

    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        if k % 2 == 0 or k % 5 == 0:
            return -1
        prod_factor = 10%k
        ans = 1
        rem = 1
        while rem:
            rem = ((rem*prod_factor)%k + 1)%k
            ans += 1

        return ans

if __name__ == '__main__':
    test_inputs = [
        ([1], 1), ([2], -1), ([5], -1), ([10], -1), ([21], 6), ([49], 42), ([63], 18)
    ]
    assert_solver(Solution().smallestRepunitDivByK, test_inputs)
