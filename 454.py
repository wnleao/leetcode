from collections import Counter, defaultdict


class SolutionTwoDicts:

    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        nums12 = defaultdict(int)
        for num1 in nums1:
            for num2 in nums2:
                nums12[num1+num2] += 1

        nums34 = defaultdict(int)
        for num3 in nums3:
            for num4 in nums4:
                nums34[num3+num4] += 1
                
        ans = 0
        for num12, count in nums12.items():
            if -num12 in nums34:
                ans += count * nums34[-num12]

        return ans


class SolutionCounterFirst:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        counter3 = Counter(nums3)
        counter4 = Counter(nums4)

        counters = sorted([(len(counter1), counter1), (len(counter2), counter2), (len(counter3), counter3), (len(counter4), counter4)])
        counters = [counter for _, counter in counters]

        nums03 = defaultdict(int)
        for n1, c1 in counters[0].items():
            for n2, c2 in counters[3].items():
                nums03[n1+n2] += c1*c2

        nums12 = defaultdict(int)
        for n1, c1 in counters[1].items():
            for n2, c2 in counters[2].items():
                nums12[n1+n2] += c1*c2
                
        ans = 0
        for num03, count in nums03.items():
            ans += count * nums12.get(-num03, 0)

        return ans



if __name__ == "__main__":
    solvers = [SolutionTwoDicts(), SolutionCounterFirst()]
    test_inputs = [
        ([[1,2], [-2,-1], [-1,2], [0,2]], 2),
        ([[0], [0], [0], [0]], 1),
    ]
    for solver in solvers:
        for input, expected in test_inputs:
            assert solver.fourSumCount(*input) == expected
