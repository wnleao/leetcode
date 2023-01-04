#
# 2244. Minimum Rounds to Complete All Tasks
# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks
#
from collections import Counter


class Solution1:

    def minimumRounds(self, tasks: list[int]) -> int:
        rounds = 0
        for v in Counter(tasks).values():
            if v == 1:
                return -1
            # or rounds += v//3 + (v%3 != 0)
            rounds += (v+2)//3

        return rounds


class Solution2:

    def minimumRounds(self, tasks: list[int]) -> int:
        rounds = sum([(v+2)//3 if v > 1 else -100001 for v in Counter(tasks).values()])
        return rounds if rounds > 0 else -1


if __name__ == "__main__":
    sol = Solution1()
    assert 4 == sol.minimumRounds([2,2,3,3,2,4,4,4,4,4])
    assert -1 == sol.minimumRounds([2,3,3])
