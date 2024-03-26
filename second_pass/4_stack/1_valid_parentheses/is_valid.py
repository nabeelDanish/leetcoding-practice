class MySolution:
    def isValid(self, s: str) -> bool:
        stack = []
        n = len(s)

        for i in range(n):
            if s[i] in ["(", "{", "["]:
                stack.append(s[i])
            elif stack:
                prev = stack.pop()

                if s[i] == ")" and prev != "(":
                    return False
                if s[i] == "}" and prev != "{":
                    return False
                if s[i] == "]" and prev != "[":
                    return False
            else:
                return False

        return len(stack) == 0

    def testIsValid(self, s, expected):
        actual = self.isValid(s)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! s: {s}, actual: {actual}, expected: {expected}")


MySolution().testIsValid("()", True)
MySolution().testIsValid("()[]{}", True)
MySolution().testIsValid("(]", False)
MySolution().testIsValid("]", False)
