from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        n = len(strs)
        for i in range(n):
            new = ''.join(sorted(strs[i]))
            map[new].append(strs[i])

        return list(map.values())

    def testGroupAnagrams(self, strs: List[str], expected: List[List[str]]):
        actual = self.groupAnagrams(strs)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! strs: {strs} actual: {actual} expected: {expected}")
