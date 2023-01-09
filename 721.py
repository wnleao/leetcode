from collections import defaultdict

from data_structures import UnionFind


class Solution:

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        uf = UnionFind(len(accounts))
        email_ids = {}
        for i, (name, *emails) in enumerate(accounts):
            for email in emails:
                if email in email_ids:
                    uf.union(email_ids[email], i)
                email_ids[email] = i
        
        id_emails = defaultdict(list)
        for email, i in email_ids.items():
            id_emails[uf.find(i)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in id_emails.items()]


if __name__ == '__main__':
    solver = Solution()
    test_inputs = [
        (
            [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]],
            sorted([["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
        ),
        (
            [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]],
            sorted([["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]])
        ),
    ]
    for input, expected in test_inputs:
        actual = solver.accountsMerge(input)
        assert sorted(actual) == expected, f'the result for {input} was {actual} but the expected is {expected}'
