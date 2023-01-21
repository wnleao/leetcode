from utils import assert_solver


class Solution:

    def restoreIpAddresses(self, s: str) -> list[str]:

        def search(sub: str, num_dots: int) -> list[str]:
            if len(sub) <= num_dots:
                return []
            if num_dots == 0:
                return [sub] if len(sub) == 1 or int(sub) <= 255 and sub[0] != '0' else []
            if sub[0] == '0':
                return ['0.' + ip for ip in search(sub[1:], num_dots-1)]

            ips = []
            i = 1
            while i <= len(sub)-num_dots:
                prefix = sub[:i]
                if int(prefix) > 255:
                    break
                prefix +=  '.'
                ips += [prefix + ip for ip in search(sub[i:], num_dots-1)]
                i += 1

            return ips

        return search(s, 3)


if __name__ == '__main__':
    test_inputs = [
        (["0000"], ["0.0.0.0"]),
        (["25525511135"], ["255.255.11.135", "255.255.111.35"]),
        (["101023"], ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
    ]
    assert_solver(Solution().restoreIpAddresses, test_inputs)
