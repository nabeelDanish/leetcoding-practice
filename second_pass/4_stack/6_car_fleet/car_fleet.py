from typing import List


class SortSolution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine positions and speed into a single list
        combined = list(zip(position, speed))

        # Sort the list based on position of the cars
        combined = sorted(combined, key=lambda x: x[0])

        n = len(combined)

        # Empty stack that will maintain all the fleets
        stack = []

        # Iterate from right to left over the cars
        # This is because the cars/fleets on the right will always be the one dictating the speed of the fleets
        for i in range(n - 1, -1, -1):
            # Push the current car on the stack
            curr_car = combined[i]
            stack.append(curr_car)

            # Check if the car that we added merges with the last fleet there was
            if len(stack) >= 2:
                last_fleet = stack[-2]
                if self.willMerge(curr_car, last_fleet, target):
                    stack.pop()

        # The total number of fleets will be the elements in the stack
        return len(stack)

    def willMerge(self, a, b, target):
        dist_a = target - a[0]
        dist_b = target - b[0]

        time_a = dist_a / a[1]
        time_b = dist_b / b[1]

        return time_a <= time_b

    def testCarFleet(self, target, position, speed, expected):
        actual = self.carFleet(target, position, speed)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! target: {target}, position: {position}, speed: {speed}, actual: {actual}, expected: {expected}")


SortSolution().testCarFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3)
SortSolution().testCarFleet(10, [3], [3], 1)
SortSolution().testCarFleet(100, [0, 2, 4], [4, 2, 1], 1)
SortSolution().testCarFleet(10, [2, 4], [3, 2], 1)
SortSolution().testCarFleet(100, [0, 4, 2], [2, 1, 3], 1)
SortSolution().testCarFleet(10, [6, 8], [3, 2], 2)
