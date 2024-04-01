from typing import List


class BruteForceSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_increased = []
        n = len(temperatures)

        for i in range(n):
            temp_increased.append(0)
            go_back = i - 1

            while go_back >= 0 and temperatures[go_back] < temperatures[i]:
                if temp_increased[go_back] == 0:
                    temp_increased[go_back] = i - go_back
                go_back -= 1

        return temp_increased

    def testDailyTemperatures(self, temperatures: List[int], expected: List[int]) -> None:
        actual: List[int] = self.dailyTemperatures(temperatures)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! temperatures: {temperatures}, actual: {actual}, expected: {expected}")


class StackSolution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        temp_increased = [0] * n
        stack = []

        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                days = i - index
                if temp_increased[index] == 0:
                    temp_increased[index] = days
                else:
                    temp_increased[index] = min(temp_increased[index], days)

            stack.append(i)

        return temp_increased

    def testDailyTemperatures(self, temperatures: List[int], expected: List[int]) -> None:
        actual: List[int] = self.dailyTemperatures(temperatures)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! temperatures: {temperatures}, actual: {actual}, expected: {expected}")


StackSolution().testDailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])
StackSolution().testDailyTemperatures([30, 40, 50, 60], [1, 1, 1, 0])
StackSolution().testDailyTemperatures([30, 60, 90], [1, 1, 0])
