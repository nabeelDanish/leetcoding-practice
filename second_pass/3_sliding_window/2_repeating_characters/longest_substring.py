class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()
        n = len(s)

        for right in range(n):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

    def testLengthOfLongestSubstring(self, s, expected):
        actual = self.lengthOfLongestSubstring(s)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! s: {s} actual: {actual} expected: {expected}")


Solution().testLengthOfLongestSubstring("abcabcbb", 3)
Solution().testLengthOfLongestSubstring("bbbbb", 1)
Solution().testLengthOfLongestSubstring("pwwkew", 3)
Solution().testLengthOfLongestSubstring("au", 2)
Solution().testLengthOfLongestSubstring("dvdf", 3)
