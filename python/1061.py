from collections import defaultdict

from utils import assert_solvers


class SolutionUnionFind:

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        union_find = {}
        def find(u: str):
            union_find.setdefault(u, u)
            if u != union_find[u]:
                union_find[u] = find(union_find[u])
            return union_find[u]

        def union(u: str, q: str):
            ru, rq = find(u), find(q)
            if ru < rq:
                union_find[rq] = ru
            else:
                union_find[ru] = rq

        for c1, c2 in zip(s1, s2):
            union(c1, c2)

        return ''.join([find(ch) for ch in baseStr])


class SolutionSets:

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        eq_dict = defaultdict(set)
        for c1, c2 in zip(s1, s2):
            eq_dict[c1].add(c1)
            eq_dict[c1].add(c2)
            eq_dict[c2].add(c1)
            eq_dict[c2].add(c2)

        for k, v in eq_dict.items():
            for ch in v:
                eq_dict[ch].update(v)

        sorted_dict = defaultdict(list)
        for k, v in eq_dict.items():
            sorted_dict[k] = sorted(v)

        ans = ''
        for ch in baseStr:
            if ch in sorted_dict:
                ans += sorted_dict[ch][0]
            else:
                ans += ch

        return ans


if __name__ == '__main__':
    solvers = [SolutionSets().smallestEquivalentString, SolutionUnionFind().smallestEquivalentString]
    test_inputs = [
        (("parker", "morris", "parser"), "makkek"),
        (("leetcode", "programs", "sourcecode"), "aauaaaaada"),
    ]
    assert_solvers(solvers, test_inputs)
