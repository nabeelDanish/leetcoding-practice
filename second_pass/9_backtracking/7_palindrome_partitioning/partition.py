from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        paths = []
        self.backtrack(s, [], paths, 0)
        return paths

    def backtrack(self, s: str, path: List[str], paths: List[List[str]], curr_ix: int):
        # if we have reached the end of the string, we have found a valid path, add it to the paths list and return
        if curr_ix == len(s):
            paths.append(path.copy())
            return

        # iterate through the string starting from the current index and check if the substring from the ith to the current index is a palindrome, 
        # if it is, we can add it to the path and continue backtracking with the next index as the current index, 
        # after backtracking we will pop the substring from the path and continue checking for other substrings
        for i in range(curr_ix, len(s)):
            if self.isPalindrome(s, curr_ix, i):
                path.append(s[curr_ix:i + 1])
                self.backtrack(s, path, paths, i + 1)
                path.pop()

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        # check if the substring s[left:right + 1] is a palindrome
        # we can check this by comparing the characters at the left and right pointers and moving them towards the center until they meet
        while left < right:
            # if the characters at the left and right pointers are not the same, then the substring is not a palindrome
            if s[left] != s[right]:
                return False

            # move the left and right pointers towards the center
            left += 1
            right -= 1
        
        # if we have checked all the characters and they are all the same, then the substring is a palindrome
        return True

    def testPartition(self, s: str, expected: List[List[str]]):
        actual = self.partition(s)
        if len(actual) == len(expected) and all([a in expected for a in actual]):
            print(f"Test Case Passed for s: {s}")
        else:
            print(f"Test Case Failed! s: {s}, actual: {actual}, expected: {expected}")


Solution().testPartition(
    "aab",
    [["a", "a", "b"], ["aa", "b"]]
)
Solution().testPartition(
    "a",
    [["a"]]
)
