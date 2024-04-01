from typing import List


class BruteForceSolution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Use to a queue and initialize it to ""
        # This will be used for breadth-first search
        from queue import Queue
        queue = Queue()
        queue.put("")

        # Initialize answer array
        all_strings = []

        # Iterate until queue is empty. This is the basic of breadth-first searching
        while queue.qsize():
            curr_string = queue.get()

            # If we have reached the limit of search which is 2 * n size string
            # Then check if it is valid. If yes then we add
            if len(curr_string) == 2 * n and self.isValid(curr_string):
                all_strings.append(curr_string)
            else:
                queue.put(curr_string + ")")  # First branch
                queue.put(curr_string + "(")  # Second branch

        return all_strings

    def isValid(self, p_string: str) -> bool:
        left_count = 0
        for i in range(len(p_string)):
            if p_string[i] == "(":
                left_count += 1
            else:
                left_count -= 1
                if left_count < 0:
                    return False  # Early stopping condition

        return left_count == 0

    def testGenerateParenthesis(self, n, expected):
        actual = self.generateParenthesis(n)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! n: {n}, actual: {actual}, expected: {expected}")


class BacktrackingSolution:
    def recursive(self, n: int, all_strings: List[str], curr_string: str, left_count: int, right_count: int):
        # Reached the limit, so we add to the list
        # And start return
        if len(curr_string) == 2 * n:
            all_strings.append(curr_string)
            return all_strings

        # Branching left
        # If We can add more left parenthesis so we add one and recurse from there
        if left_count < n:
            curr_string += "("
            self.recursive(n, all_strings, curr_string, left_count + 1, right_count)
            curr_string = curr_string[:-1]  # Remove the last character

        # Branching Right
        # If we number of left is more than right, we can add a right parenthesis
        if right_count < left_count:
            curr_string += ")"
            self.recursive(n, all_strings, curr_string, left_count, right_count + 1)
            curr_string = curr_string[:-1]  # Remove the last character

        return all_strings

    def generateParenthesis(self, n: int) -> List[str]:
        return self.recursive(n, [], "", 0, 0)

    def testGenerateParenthesis(self, n, expected):
        actual = self.generateParenthesis(n)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! n: {n}, actual: {actual}, expected: {expected}")


BacktrackingSolution().testGenerateParenthesis(3, ["((()))", "(()())", "(())()", "()(())", "()()()"])
BacktrackingSolution().testGenerateParenthesis(1, ["()"])
