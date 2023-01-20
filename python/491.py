class Solution:
    
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        seqs = set()
        for num in nums:
            new_seqs = set()
            for seq in seqs:
                if num >= seq[-1]:
                    new_seqs.add(seq + (num, ))

            new_seqs.update(seqs)
            seqs = new_seqs
            seqs.add((num, ))

        return [list(seq) for seq in seqs if len(seq) > 1]


if __name__ == '__main__':
    expected = sorted([[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]])
    assert expected == sorted(Solution().findSubsequences([4,6,7,7]))
