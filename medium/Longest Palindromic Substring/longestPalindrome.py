def longestPalindrome(s: str) -> str:
    def checkPalindrome(i, j) -> bool:
        left = i
        right = j - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True

    for length in range(len(s), 0, -1):
        for start in range(len(s) - length + 1):
            if checkPalindrome(start, start + length):
                return s[start : start + length]

    return ""


def testLongestPalindrome(s: str, expected: str):
    result = longestPalindrome(s)
    if result == expected:
        print("Test Case Passed!")
    else:
        print(f"Test Case Failed: s: {s}, result: {result}, expected: {expected}")


testLongestPalindrome("babad", "bab")
testLongestPalindrome("cbbd", "bb")
