
# Longest Consecutive Sequence

## Problem Statement
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in $O(n)$ complexity.

## Constraints
- $1 \leq n \leq 10^5$ where $n$ is the length of the input array
- Each element is an integer (can be positive, negative, or zero)
- The sequence does not need to be sorted in the input

## Solution 1: Hash Set Approach

### Idea
Use a hash set to quickly check for the existence of elements. For each number, only start counting a sequence if it is the beginning (i.e., if `num - 1` is not in the set). Then, count up for consecutive numbers.

### Algorithm
1. Insert all numbers into a set for $O(1)$ lookups.
2. For each number, check if it is the start of a sequence (`num - 1` not in set).
3. If so, count the length of the sequence by checking consecutive numbers (`num + 1`, `num + 2`, ...).
4. Track the maximum sequence length found.

### Code
```python
from typing import List

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		hashmap = set(nums)
		longest = 0

		for num in hashmap:
			if num - 1 not in hashmap:
				current_num = num
				n = 1

				while current_num + 1 in hashmap:
					current_num += 1
					n += 1

				longest = max(longest, n)

		return longest
```

### Complexity
- Time: $O(n)$ (each number is processed at most twice)
- Space: $O(n)$ (for the set)

### Example
Input: `[100, 4, 200, 1, 3, 2]`
Output: `4` (sequence: `1, 2, 3, 4`)

Input: `[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]`
Output: `9` (sequence: `0, 1, 2, 3, 4, 5, 6, 7, 8`)

---
You can add more solutions (e.g., sorting-based, union-find) if needed, but the hash set approach is optimal for $O(n)$.
