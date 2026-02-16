# Container With Most Water

## Problem Statement
Given an array `height` of non-negative integers, each representing the height of a vertical line on the x-axis, find two lines that together with the x-axis form a container that holds the most water. Return the maximum amount of water a container can store.

## Constraints
- $2 \leq$ length of `height` $\leq 10^5$
- $0 \leq$ height[i] $\leq 10^4$

## Solution: Two Pointer Approach

### Idea
Use two pointers, one at the start and one at the end. Calculate the area formed by the lines at these pointers. Move the pointer with the smaller height inward, since it limits the area. Repeat until the pointers meet.

### Algorithm
1. Initialize `left` at 0 and `right` at $n-1$.
2. While `left < right`:
	- Calculate area: `min(height[left], height[right]) * (right - left)`.
	- Update maximum area found.
	- Move the pointer with the smaller height inward.
3. Return the maximum area.

### Code
```python
from typing import List

class Solution:
	def maxArea(self, height: List[int]) -> int:
		most_water = 0
		n = len(height)
		left = 0
		right = n - 1

		while (left < right):
			water = min(height[left], height[right]) * abs(right - left)
			most_water = max(water, most_water)

			if height[left] < height[right]:
				left += 1
			else:
				right -= 1

		return most_water
```

### Complexity
- Time: $O(n)$
- Space: $O(1)$

### Example
Input: `[1, 8, 6, 2, 5, 4, 8, 3, 7]`
Output: `49`

Input: `[1, 1]`
Output: `1`

---
This two-pointer approach efficiently finds the maximum area, matching the provided code implementation.
