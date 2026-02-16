# Two Sum

## Problem Statement
Given a sorted array of integers, find two numbers such that they add up to a specific target number. Return their indices (1-based). Assume exactly one solution exists.

## Constraints
- $1 \leq$ length of array $\leq 10^5$
- Array is sorted in non-decreasing order
- Only one valid answer exists

## Solution: Two Pointer Approach

### Idea
Use two pointers, one at the start (`left`) and one at the end (`right`). Move the pointers inward based on the sum compared to the target. Skip duplicate values to avoid redundant checks.

### Algorithm
1. Initialize `left` at 0 and `right` at $n-1$.
2. While `left <= right`:
	- Skip duplicates for `left` and `right`.
	- Calculate `numbers[left] + numbers[right]`.
	- If sum equals target, return `[left + 1, right + 1]`.
	- If sum < target, increment `left`.
	- If sum > target, decrement `right`.

### Code
```python
from typing import List

class Solution:
	def twoSum(self, numbers: List[int], target: int) -> List[int]:
		n = len(numbers)
		left = 0
		right = n - 1

		while (left <= right and left < n and right > 0):
			while left > 0 and numbers[left] == numbers[left - 1]:
				left += 1

			while right < n - 1 and numbers[right] == numbers[right + 1]:
				right -= 1

			calc = numbers[left] + numbers[right]

			if calc == target:
				return [left + 1, right + 1]

			if calc < target:
				left += 1

			if calc > target:
				right -= 1
```

### Complexity
- Time: $O(n)$
- Space: $O(1)$

### Example
Input: `[2, 7, 11, 15]`, target: `9`
Output: `[1, 2]`

Input: `[2, 3, 4]`, target: `6`
Output: `[1, 3]`

Input: `[-1, 0]`, target: `-1`
Output: `[1, 2]`

---
This two-pointer approach efficiently finds the pair in a sorted array, matching the provided code implementation.
