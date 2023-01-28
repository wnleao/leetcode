class SummaryRanges:

    def __init__(self):
        self.max_value = 10000
        # keeps track of added numbers
        self.values: list[bool] = [False]*(self.max_value + 1)
        # makes it easier to retrieve an interval given a starting point
        self.starts: dict[int, int] = {}
        # makes it easier to retrieve an interval given an ending point
        self.ends: dict[int, int] = {}
        # cache the disjoint intervals 
        # Whenever we add a new number, the cache will be cleared
        self.cache: list[tuple[int, int]] = []

    def addNum(self, value: int) -> None:
        if self.values[value]:
            # The number has already been added!
            return 
        
        self.cache = []
        self.values[value] = True

        # We need to check if this number will cause a merge.
        # To merge two intervals we need to update the starts 
        # and ends dicts. We will only need to merge two intervals,
        # because we should consider the following cases:
        # 1. left_interval + value (value is the new end)
        # 2. value + right_inverval (value is the new start)
        # 3. left_inverval + right_interval (value is in the middle)
        new_start = new_end = value
        lid = value - 1
        if lid >= 0 and self.values[lid]:
            new_start = self.ends.pop(lid)            

        rid = value + 1
        if rid <= self.max_value and self.values[rid]:
            new_end = self.starts.pop(rid)

        self.starts[new_start] = new_end
        self.ends[new_end] = new_start

    def getIntervals(self) -> list[tuple[int, int]]:
        if not self.cache and self.starts:
            self.cache = sorted(self.starts.items()) 
        return self.cache
