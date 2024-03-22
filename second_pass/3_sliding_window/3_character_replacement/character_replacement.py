class BruteForceSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        n = len(s)

        max_length = 1

        # The first two loop generate all the possible substrings
        for start in range(n):
            for end in range(start + 1, n):
                # We need to count the frequencies of all the characters in this substring range
                char_counts = defaultdict(int)
                for i in range(start, end + 1):
                    char_counts[s[i]] += 1

                # Find the character that has the maximum count
                # This character is the target, and all other characters will need to be changed to this one
                # For the substring to be valid
                max_char = max(char_counts, key=char_counts.get)
                max_freq = char_counts[max_char]

                # Compute the sum of the frequencies of all the other characters except for the max one
                # This should be less than or equals to k otherwise we will need to do more operations on the string
                # And it will not be valid
                sum_other_freq = sum(freq for char, freq in char_counts.items() if char != max_char)
                if sum_other_freq <= k:
                    max_length = max(max_length, end - start + 1)

        return max_length

    def testCharacterReplacement(self, s, k, expected):
        actual = self.characterReplacement(s, k)
        if actual == expected:
            print('Test Case Passed!')
        else:
            print(f"Test Case Failed! s: {s} k: {k} actual: {actual} expected: {expected}")


class BinarySearchSlidingWindowSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        # These ranges of the binary search are for the length of the substring
        left = 1
        right = n + 1

        # Doing a binary search on the length of the substring
        while (left + 1 < right):
            mid = left + (right - left) // 2
            if self.isValidSubstring(s, k, mid):  # check if we can make a valid substring of this length
                # If we do find a valid substring, then we need to go right because
                # if i is valid then i - 1, i - 2, ... 3, 2, 1 are all valid lengths
                left = mid
            else:
                # If this length can't make valid substring then we go left because we need to
                # Reduce the length. If i can't be valid so can't i + 1, i + 2, ... n are valid
                right = mid

        # We return left because it will point to the
        # Most valid length of the substring
        return left

    def isValidSubstring(self, s: str, k: int, mid: int):
        from collections import defaultdict
        n = len(s)
        char_counts = defaultdict(int)

        # First we build the frequency map
        # For the first sliding window which starts from 0 and goes till mid
        for i in range(0, mid):
            char_counts[s[i]] += 1

        # Now we can check if this window is valid
        # And if not, we can move it one step to the right
        start = 0
        end = mid - 1
        while (end < n):
            # First check if this window is valid or not using the same
            # logic we used in brute force
            max_char = max(char_counts, key=char_counts.get)
            max_freq = char_counts[max_char]

            # Now check if this plus the operations k can be greater than the length mid
            if max_freq + k >= mid:
                return True

            # Otherwise we move the sliding window one unit to the left
            char_counts[s[start]] -= 1
            if end + 1 < n:
                char_counts[s[end + 1]] += 1

            start += 1
            end += 1

        # Return false if we couldn't find a valid substring
        return False

    def testCharacterReplacement(self, s, k, expected):
        actual = self.characterReplacement(s, k)
        if actual == expected:
            print('Test Case Passed!')
        else:
            print(f"Test Case Failed! s: {s} k: {k} actual: {actual} expected: {expected}")


class SlidingWindowSlowSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        # This approach will work by considering each alphabet the target
        # and we will create a growing/shrinking sliding window to find the valid substring
        all_letters = set(s)

        # Iterate over each unique letter, maintaining the count of the target letter that we see
        max_length = 1
        for target in all_letters:
            # Count maintains the count of the target in the sliding window
            # between start and end
            start = end = count = 0
            n = len(s)

            # Iterate end to the end of the given string
            for end in range(n):
                # If end is at the target letter, we just increase the count
                if s[end] == target:
                    count += 1

                # If the window is valid, we move end forward
                # But while the window is invalid, we move the start forward
                # And decrease the length of the substring until the window gets valid again
                while not self.isWindowValid(start, end, count, k):
                    # If start is currently at the target letter
                    # We need to decrease its count since it will be gone once the window moves forward
                    if s[start] == target:
                        count -= 1
                    start += 1

                # Now that the window is valid, we compare it to the max length
                max_length = max(max_length, end - start + 1)

        return max_length

    def isWindowValid(self, start: int, end: int, count: int, k: int) -> bool:
        return (end + 1) - start - count <= k

    def testCharacterReplacement(self, s, k, expected):
        actual = self.characterReplacement(s, k)
        if actual == expected:
            print('Test Case Passed!')
        else:
            print(f"Test Case Failed! s: {s} k: {k} actual: {actual} expected: {expected}")


class SlidingWindowFast:
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize start and end values so that the first window we get is always valid
        from collections import defaultdict
        start = 0
        n = len(s)
        char_counts = defaultdict(int)
        max_freq = 0
        max_length = 0

        # We are going to move the end all the way to the end of the string
        for end in range(n):
            # First update the counts since we just moved end one step forward
            char_counts[s[end]] += 1
            # Update the maximum frequency against the character we just added in the window
            max_freq = max(max_freq, char_counts[s[end]])

            # Now we check if this sliding window is valid or not
            is_valid = end - start + 1 - max_freq <= k
            if not is_valid:
                # If it is not valid, we move start one step forward
                # and decrease this character count
                char_counts[s[start]] -= 1
                start += 1

            # Compute the max length of the substring now. If l - 1 was valid, and l was not, than
            # By moving start one step forward we restored the length of the substring to l - 1 again (which we know is valid)
            max_length = max(max_length, end - start + 1)

        return max_length

    def testCharacterReplacement(self, s, k, expected):
        actual = self.characterReplacement(s, k)
        if actual == expected:
            print('Test Case Passed!')
        else:
            print(f"Test Case Failed! s: {s} k: {k} actual: {actual} expected: {expected}")


SlidingWindowFast().testCharacterReplacement("ABAB", 2, 4)
SlidingWindowFast().testCharacterReplacement("ABAA", 0, 2)
SlidingWindowFast().testCharacterReplacement("AABABBA", 1, 4)
