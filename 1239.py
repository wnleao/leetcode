class Solution:
    
    def maxLength(self, arr: list[str]) -> int:
        N = len(arr)
        arr.sort(reverse=True, key=len)
        max_len_all = len(set(''.join(arr)))

        def explore(i: int, visited: set):
            if i == N or len(visited) == max_len_all:
                return len(visited)

            new_visited = set(arr[i])
            new_visited.update(visited)

            max_len = 0
            new_len = len(new_visited)
            if new_len == len(visited) + len(arr[i]):
                # may use this word...
                max_len = max(max_len, explore(i+1, new_visited))
                if max_len == max_len_all:
                    return max_len_all

            # do not use current word...
            max_len = max(max_len, explore(i+1, visited))
            if max_len == max_len_all:
                return max_len_all

            return max_len

        return explore(0, set())


class SolutionCleaner:
    
    def maxLength(self, arr: list[str]) -> int:
        N = len(arr)
        arr.sort(reverse=True, key=len)
        max_len_all = len(set(''.join(arr)))

        def explore(i: int, visited: set):
            if i == N or len(visited) == max_len_all:
                return len(visited)

            explore_sets = [visited]

            new_visited = set(arr[i])
            new_visited.update(visited)
            if len(new_visited) == len(visited) + len(arr[i]):
                # may use this word...
                explore_sets.append(new_visited)

            max_len = 0
            for explore_set in explore_sets:
                max_len = max(max_len, explore(i+1, explore_set))
                if max_len == max_len_all:
                    return max_len_all

            return max_len

        return explore(0, set())


if __name__ == "__main__":
    sol = Solution()
    assert 4 == sol.maxLength(["un","iq","ue"])
    assert 6 == sol.maxLength(["cha","r","act","ers"])
    assert 26 == sol.maxLength(["abcdefghijklmnopqrstuvwxyz"])
