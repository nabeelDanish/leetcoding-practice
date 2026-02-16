# Valid Palindrome

## Problem Statement
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

## Constraints
- $1 \leq$ length of string $\leq 10^5$
- String may contain spaces, punctuation, and mixed case letters

## Solution: Regex Sanitization and Center Comparison

### Idea
First, sanitize the string by removing all non-alphanumeric characters and converting it to lowercase using regex. Then, compare characters from both ends towards the center to check for palindrome.

### Algorithm
1. Use regex to remove all non-alphanumeric characters and convert the string to lowercase.
2. Set two pointers: `left` at the start, `right` at the end.
3. For each index up to the center, compare the characters at `left` and `right`.
4. If any pair does not match, return `False`. If all pairs match, return `True`.

### Code
```python
class Solution:
	def isPalindrome(self, s: str) -> bool:
		import re
		import math

		sanitized = re.sub(r'[\W_]', "", s).lower()

		n = len(sanitized)
		center = math.floor(n / 2)

		left = 0
		right = n - 1

		for i in range(center):
			a = sanitized[left]
			b = sanitized[right]

			if a != b:
				return False

			left += 1
			right -= 1

		return True
```

### Complexity
- Time: $O(n)$ (for sanitization and comparison)
- Space: $O(n)$ (for the sanitized string)

### Example
Input: `"A man, a plan, a canal: Panama"`
Output: `True`
Explanation: After sanitization, the string becomes "amanaplanacanalpanama", which is a palindrome.

Input: `"race a car"`
Output: `False`

---
This approach uses regex for preprocessing and compares characters from both ends, matching the provided code implementation.
