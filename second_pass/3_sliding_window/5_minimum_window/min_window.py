class SlidingWindowSolution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        import math
        n = len(s)
        m = len(t)

        if n < m:
            return ""

        t_map = defaultdict(int)
        for i in range(m):
            t_map[t[i]] += 1

        s_map = defaultdict(int)

        start = 0
        end = 0

        min_length = math.inf
        min_start = 0
        min_end = 0

        while end < n:
            if self.isSubset(s_map, t_map):
                curr_len = end - start + 1

                if curr_len < min_length:
                    min_length = curr_len
                    min_start = start
                    min_end = end

                s_map[s[start]] -= 1
                start += 1
            else:
                s_map[s[end]] += 1
                end += 1

        while self.isSubset(s_map, t_map):
            curr_len = end - start + 1

            if curr_len < min_length:
                min_length = curr_len
                min_start = start
                min_end = end

            s_map[s[start]] -= 1
            start += 1

        return s[min_start:min_end]

    def isSubset(self, super_dict: dict, sub_dict: dict) -> bool:
        for key, value in sub_dict.items():
            if not key in super_dict:
                return False
            if super_dict[key] < sub_dict[key]:
                return False

        return True

    def testMinWindow(self, s, t, expected):
        actual = self.minWindow(s, t)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! s: {s}, t: {t}, actual: {actual}, expected: {expected}")


SlidingWindowSolution().testMinWindow("ADOBECODEBANC", "ABC", "BANC")
SlidingWindowSolution().testMinWindow("a", "a", "a")
SlidingWindowSolution().testMinWindow("a", "aa", "")
