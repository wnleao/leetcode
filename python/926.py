from utils import assert_solver


class Solution:

    def minFlipsMonoIncr(self, s: str) -> int:
        idx = s.find('1')
        if idx < 0:
            return 0

        flips = 0
        ones = 0
        for ch in s[idx:]:
            if ch == '1':
                ones += 1
            elif ones:
                ones -= 1
                flips += 1

        return flips


if __name__ == '__main__':
    test_inputs = [
        (["00110"], 1),
        (["010110"], 2),
        (["00011000"], 2),
        (["000100001000"], 2),
        (["0000000000"], 0),
        (["1"], 0),
        (["0"], 0),
    ]
    assert_solver(Solution().minFlipsMonoIncr, test_inputs)
