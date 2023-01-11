from utils import assert_solver


class Solution:

    def minSwapsCouples(self, row: list[int]) -> int:
        people = [0]*len(row)
        for seat, person_id in enumerate(row):
            people[person_id] = seat

        min_swaps = 0
        for i in range(0, len(row), 2):
            id0, id1 = row[i], row[i+1]
            if abs(id0-id1) == 1 and (id0+id1 - 1)%4 == 0:
                continue

            min_swaps += 1
            idx = id0 + 1 if id0 % 2 == 0 else id0 - 1
            row[people[idx]] = id1
            people[id1] = people[idx]

        return min_swaps


if __name__ == '__main__':
    test_inputs = [
        ([[0,2,1,3]], 1),
        ([[3,2,0,1]], 0),
    ]
    assert_solver(Solution().minSwapsCouples, test_inputs)
