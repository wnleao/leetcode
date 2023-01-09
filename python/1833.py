class Solution:

    def maxIceCream(self, costs: list[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            coins -= costs[i]
            if coins < 0:                
                return i

        return len(costs)


if __name__ == "__main__":
    sol = Solution()
    assert 4 == sol.maxIceCream([1,3,2,4,1], 7)
    assert 0 == sol.maxIceCream([10,6,8,7,7,8], 5)
    assert 6 == sol.maxIceCream([1,6,3,1,2,5], 20)
