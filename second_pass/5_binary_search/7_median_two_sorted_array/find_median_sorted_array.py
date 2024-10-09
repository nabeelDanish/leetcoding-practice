from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthSmallestElement(k, a_start, a_end, b_start, b_end):
            # Add the stopping condition which is to check if a segment of one array is empty
            # This means we have passed over all the elements of that array
            # In this case, the kth smallest element is the kth element in the other remaining segment
            if a_start > a_end:
                # The reason for k - start is because k remains unchanged throughout the recursion
                # So the kth smallest element would be remaining_array[k - 1] but we need to offset the segment
                # from the other array that was discarded to basically "go over" the numbers that smaller than the ones in the remaining array
                return nums2[k - a_start]
            if b_start > b_end:
                return nums1[k - b_start]

            # Find the middle indexes and the middle values
            a_index = (a_start + a_end) // 2
            b_index = (b_start + b_end) // 2
            a_value = nums1[a_index]
            b_value = nums2[b_index]

            # Now we need to determine in which combined half is k going to be in
            # So we check the combined a_index + b_index to see if it is less than k
            # If k is in the right half than we need to remove the smaller of the left halves
            if a_index + b_index < k:
                if a_value > b_value:
                    return findKthSmallestElement(k, a_start, a_end, b_index + 1, b_end)  # B's smaller left half is removed
                else:
                    return findKthSmallestElement(k, a_index + 1, a_end, b_start, b_end)  # A's smaller left half is removed
            # Otherwise, we need to remove the larger of the right halves
            else:
                if a_value > b_value:
                    return findKthSmallestElement(k, a_start, a_index - 1, b_start, b_end)  # A's bigger right half is removed
                else:
                    return findKthSmallestElement(k, a_start, a_end, b_start, b_index - 1)  # B's bigger right half is removed

        # End of function
        # Essentially, now we need to just find the smallest middle element (or two smallest middle elements)
        # To find the median
        nA = len(nums1)
        nB = len(nums2)
        n = nA + nB

        if n % 2:
            return findKthSmallestElement(n // 2, 0, nA - 1, 0, nB - 1)
        else:
            return (findKthSmallestElement(n // 2 - 1, 0, nA - 1, 0, nB - 1) + findKthSmallestElement(n // 2, 0, nA - 1, 0, nB - 1)) / 2

    def testFindMedianSortedArrays(self, nums1: List[int], nums2: List[int], expected: float):
        actual = self.findMedianSortedArrays(nums1, nums2)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! nums1: {nums1} nums2: {nums2} actual: {actual} expected: {expected}")


Solution().testFindMedianSortedArrays([2, 4, 8, 9, 11, 15], [1, 6, 7, 10, 13, 18], 8.5)
Solution().testFindMedianSortedArrays([1, 3], [2], 2.0)
Solution().testFindMedianSortedArrays([1, 2], [3, 4], 2.5)
