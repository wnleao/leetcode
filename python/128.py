class Solution1:

    def longestConsecutive(self, nums: list[int]) -> int:
        max_size = 0
        nums_set = set(nums)
        for num in nums_set:
            if num-1 in nums_set:
                continue
            size = 0
            while num in nums_set:
                num += 1
                size += 1
            
            max_size = max(max_size, size)

        return max_size


class Solution2:

    def longestConsecutive(self, nums: list[int]) -> int:
        max_size = 0
        starts, ends = {}, {}
        for num in nums:
            if num in starts or num in ends:
                continue

            start, end = num, num
            if num+1 in starts and num-1 in ends:
                # join sequences
                start = ends[num-1]
                end = starts[num+1]
                #del ends[num-1]
                #del starts[num+1]
            elif num+1 in starts:
                # new start
                start = num
                end = starts[num+1]
                #del starts[num+1]
            elif num-1 in ends:
                # new end
                end = num
                start = ends[num-1]
                #del ends[num-1]
            
            # update sequence starts and ends
            starts[start] = end
            ends[end] = start
            max_size = max(max_size, end - start + 1)

        return max_size


if __name__ == "__main__":
    solvers = [Solution1(), Solution2()]
    test_inputs = [
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
    ]
    for solver in solvers:
        for input, expected in test_inputs:
            assert solver.longestConsecutive(input) == expected
