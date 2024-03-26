from typing import List


class MySolution:
    operators = ["+", "-", "*", "/"]

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        n = len(tokens)

        for i in range(n):
            if self.isNumber(tokens[i]):
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()
                calc = self.calculate(a, b, tokens[i])
                stack.append(calc)

        return stack.pop()

    def isNumber(self, token: str) -> bool:
        return token not in self.operators

    def isOperator(self, token: str) -> bool:
        return token in self.operators

    def calculate(self, a: int, b: int, operator: str) -> int:
        if operator == "+":
            return a + b
        if operator == "-":
            return a - b
        if operator == "*":
            return a * b
        if operator == "/":
            return int(a / b)

    def testEvalRPN(self, tokens, expected):
        actual = self.evalRPN(tokens)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! tokens: {tokens}, actual: {actual}, expected: {expected}")


MySolution().testEvalRPN(["2", "1", "+", "3", "*"], 9)
MySolution().testEvalRPN(["4", "13", "5", "/", "+"], 6)
MySolution().testEvalRPN(["4", "13", "5", "/", "+"], 6)
MySolution().testEvalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)
