class SolutionGreedy:
    """Greedy solution O(n) that only checks gas - cost and keeps track of the difference."""

    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        tank = 0
        station_idx = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                tank = 0
                station_idx = i+1

        return station_idx


class SolutionEveryRoute:
    """Intuitive solution O(n^2) that checks every possible route."""

    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        N = len(gas)
        def check_route(i: int):
            tank = 0            
            for _ in range(N):
                tank += gas[i] - cost[i]
                if tank < 0:
                    return False

                i = i+1 if i < N-1 else 0

            return True

        for i in range(N):
            if check_route(i):
                return i

        return -1


if __name__ == "__main__":
    solvers = [SolutionGreedy(), SolutionEveryRoute()]
    test_inputs = [
        ([[1,2,3,4,5], [3,4,5,1,2]], 3),
        ([[2,3,4], [3,4,3]], -1),
    ]
    for solver in solvers:
        for input, expected in test_inputs:
            assert solver.canCompleteCircuit(*input) == expected
