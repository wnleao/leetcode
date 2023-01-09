class UnionFind:

    def __init__(self, n: int):
        self.roots = [i for i in range(n)]
        self.sizes = [1]*n
        self.components = n
    
    def find(self, p: int):
        root = p
        while self.roots[root] != root:
            root = self.roots[root]

        # path compression
        while p != root:
            next = self.roots[p]
            self.roots[p] = root
            p = next

        return root
    
    def union(self, p: int, q: int) -> bool:
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return False

        if self.sizes[root_p] > self.sizes[root_q]:
            self.roots[root_q] = root_p
            self.sizes[root_p] += self.sizes[root_q]
        else:
            self.roots[root_p] = root_q
            self.sizes[root_q] += self.sizes[root_p]

        self.components -= 1

        return True

    def connected(self, p: int, q: int) -> bool:
        return self.find(p) == self.find(q)

    def size(self, p: int) -> int:
        return self.size(p)

    def __len__(self) -> int:
        return self.components
