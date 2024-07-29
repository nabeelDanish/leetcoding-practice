from typing import List


class FirstSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        largest_rectangle = 0

        # Iterate over all combinations of the base length
        # Including the length of the complete list
        for base_len in range(1, n + 1):
            for start in range(0, n - base_len + 1):
                end = start + base_len
                curr_area = base_len * min(heights[start:end])
                largest_rectangle = max(largest_rectangle, curr_area)

        return largest_rectangle


    def testLargestRectangleArea(self, heights, expected):
        actual = self.largestRectangleArea(heights)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! heights: {heights}, actual: {actual}, expected: {expected}")

class DivideAndConquerSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.calculateArea(heights, 0, len(heights) - 1)

    def calculateArea(self, heights: List[int], start: int, end: int) -> int:
        if start > end:
            return 0
        
        min_h = heights[start]
        min_index = start
        for i in range(start, end + 1):
            if heights[i] < min_h:
                min_h = heights[i]
                min_index = i

        curr_area = min_h * (end - start + 1)
        left_max_area = self.calculateArea(heights, start, min_index - 1)
        right_max_area = self.calculateArea(heights, min_index + 1, end)

        return max(curr_area, left_max_area, right_max_area)


    def testLargestRectangleArea(self, heights, expected):
        actual = self.largestRectangleArea(heights)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! heights: {heights}, actual: {actual}, expected: {expected}")

class StackSolution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        HEIGHT = 0
        INDEX = 1
        
        stack = [[-1, -1]]
        left_index = 0
        n = len(heights)
        largest_area = heights[0]
        
        while left_index < n:
            top = stack[-1]
            
            if top[HEIGHT] <= heights[left_index] or left_index == 0:
                stack.append([heights[left_index], left_index])
            else:
                last_index = -1
                while top[INDEX] != -1 and top[HEIGHT] > heights[left_index]:
                    last_element = stack.pop()
                    curr_area = last_element[HEIGHT] * (left_index - last_element[INDEX])
                    largest_area = max(curr_area, largest_area)
                    last_index = last_element[INDEX]
                    top = stack[-1]

                stack.append([heights[left_index], last_index])

            left_index += 1

        
        top = stack[-1]
        while top[INDEX] != -1:
            last_element = stack.pop()
            curr_area = last_element[HEIGHT] * (n - last_element[INDEX])
            largest_area = max(curr_area, largest_area)
            top = stack[-1]

        return largest_area
    
    def testLargestRectangleArea(self, heights, expected):
        actual = self.largestRectangleArea(heights)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! heights: {heights}, actual: {actual}, expected: {expected}")


StackSolution().testLargestRectangleArea([2, 1, 5, 6, 2, 3], 10)
StackSolution().testLargestRectangleArea([2, 4], 4)
StackSolution().testLargestRectangleArea([1], 1)
StackSolution().testLargestRectangleArea([1,1], 2)
StackSolution().testLargestRectangleArea([4,2], 4)
StackSolution().testLargestRectangleArea([2,1,2], 3)
StackSolution().testLargestRectangleArea([3,6,5,7,4,8,1,0], 20)