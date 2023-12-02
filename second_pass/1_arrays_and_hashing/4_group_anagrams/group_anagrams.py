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
