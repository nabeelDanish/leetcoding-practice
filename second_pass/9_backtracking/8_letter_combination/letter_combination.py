from typing import List


class Solution:
    _number_to_letter = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    def letterCombinations(self, digits: str) -> List[str]:
        combination = []
        combinations = []

        self.backtrack(digits, 0, combination, combinations)

        return combinations

    def backtrack(self, digits: str, curr_ix: int, combination: List[str], combinations: List[str]):
        # check if we have reached the end of the string
        # we add the combination that we have to the list
        if curr_ix == len(digits):
            word = ''.join(c for c in combination)
            combinations.append(word)
            return

        # if not, iterate over the list of letters this number has, append it to the combination, and continue from there
        letters = self._number_to_letter[digits[curr_ix]]
        for letter in letters:
            combination.append(letter)
            self.backtrack(digits, curr_ix + 1, combination, combinations)
            combination.pop()

        return

    def testLetterCombination(self, digits: str, expected: List[str]):
        actual = self.letterCombinations(digits)
        if len(actual) == len(expected) and all([a in expected for a in actual]):
            print(f"Test Case Passed for digits: {digits}")
        else:
            print(f"Test Case Failed! digits: {digits}, actual: {actual}, expected: {expected}")


Solution().testLetterCombination(
    "23",
    ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
)
Solution().testLetterCombination(
    "2",
    ["a", "b", "c"]
)
