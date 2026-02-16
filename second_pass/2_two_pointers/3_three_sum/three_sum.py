from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        # Sort the array to make it easier to skip duplicates and use two pointers
        nums = sorted(nums)
        n = len(nums)

        # Iterate through the array, fixing one element and using two pointers to find pairs that sum to the negative of the fixed element
        for i in range(n - 2):
            # Skip duplicate elements to avoid duplicate triplets in the output
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Use two pointers to find pairs that sum to the negative of the fixed element
            start = i + 1
            end = n - 1
            target = 0 - nums[i]

            # Move the start and end pointers towards each other to find pairs that sum to the target
            while (start < end):
                sum = nums[start] + nums[end]

                # If the sum of the two pointers equals the target, we found a triplet
                if sum == target:
                    output.append([nums[i], nums[start], nums[end]])

                    # Skip duplicate elements to avoid duplicate triplets in the output
                    while (start < n - 1 and nums[start] == nums[start + 1] and start < end):
                        start += 1

                    # Skip duplicate elements to avoid duplicate triplets in the output
                    while (end > 1 and nums[end] == nums[end - 1] and start < end):
                        end -= 1

                    # Move both pointers to continue searching for other pairs
                    start += 1
                    end -= 1

                # If the sum of the two pointers is less than the target, we need to increase the sum by moving the start pointer to the right
                elif sum < target:
                    start += 1

                # If the sum of the two pointers is greater than the target, we need to decrease the sum by moving the end pointer to the left
                else:
                    end -= 1

        return output

    def testThreeSum(self, nums, expected):
        actual = self.threeSum(nums)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed nums: {nums} actual: {actual} expected: {expected}")


Solution().testThreeSum([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]])
Solution().testThreeSum([0, 1, 1], [])
Solution().testThreeSum([0, 0, 0], [[0, 0, 0]])
