class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        import math

        sanitized = re.sub(r'[\W_]', "", s).lower()

        n = len(sanitized)
        center = math.floor(n / 2)

        left = 0
        right = n - 1

        for i in range(center):
            a = sanitized[left]
            b = sanitized[right]

            if a != b:
                return False

            left += 1
            right -= 1

        return True

    def testIsPalindrome(self, s, expected):
        actual = self.isPalindrome(s)
        if actual == expected:
            print("Test Case Passed")
        else:
            print(f"Test Case Failed! s: {s} actual: {actual} expected: {expected}")


Solution().testIsPalindrome("A man, a plan, a canal: Panama", True)
Solution().testIsPalindrome("race a car", False)
Solution().testIsPalindrome(" ", True)
