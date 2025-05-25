from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.backtrack(candidates, target, 0, [], result)
        return result

    def backtrack(self, candidates: List[int], target: int, start: int, path: List[int], result: List[List[int]]) -> None:
        if target == 0:
            result.append(path[:])
            return
        if target < 0:
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            self.backtrack(candidates, target - candidates[i], i + 1, path, result)
            path.pop()

    def testCombinationSum2(self, candidates: List[int], target: int, expected: List[List[int]]) -> None:
        result = self.combinationSum2(candidates, target)
        assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"
        print(f"Test passed for candidates={candidates}, target={target}")


Solution().testCombinationSum2(
    candidates=[10, 1, 2, 7, 6, 1, 5],
    target=8,
    expected=[[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
)
Solution().testCombinationSum2(
    candidates=[2, 5, 2, 1, 2],
    target=5,
    expected=[[1, 2, 2], [5]]
)
