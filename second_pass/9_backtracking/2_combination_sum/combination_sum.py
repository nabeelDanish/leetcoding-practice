from typing import List, Dict


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        if not candidates or target < 0:
            return results
        candidates.sort()
        self.backtrack(candidates, target, 0, [], results)

        return results

    def backtrack(self, candidates: List[int], target: int, start: int, path: List[int], result: List[List[int]]) -> None:
        if target == 0:
            result.append(path.copy())
            return
        if target < 0:
            return

        for i in range(start, len(candidates)):
            candidate = candidates[i]
            path.append(candidate)
            self.backtrack(candidates, target - candidate, i, path, result)
            path.pop()

    def testCombinationSum(self, candidates: List[int], target: int, expected: List[List[int]]) -> None:
        result = self.combinationSum(candidates, target)
        assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"
        print(f"Test passed for candidates={candidates}, target={target}")


Solution().testCombinationSum(
    [2, 3, 6, 7],
    7,
    [[2, 2, 3], [7]]
)
Solution().testCombinationSum(
    [2, 3, 5],
    8,
    [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
)
Solution().testCombinationSum(
    [2],
    1,
    []
)
