class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphabets = [0] * 26

        offset = ord("a")

        for i in range(len(s)):
            alphabets[ord(s[i]) - offset] += 1
            alphabets[ord(t[i]) - offset] -= 1

        for j in range(26):
            if alphabets[j] != 0:
                return False

        return True

    def testIsAnagram(self, s, t, expected) -> bool:
        actual = self.isAnagram(s, t)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! s: {s} t: {t} actual: {actual} expected: {expected}")


solution = Solution()
solution.testIsAnagram("anagram", "nagaram", True)
solution.testIsAnagram("rat", "car", False)
