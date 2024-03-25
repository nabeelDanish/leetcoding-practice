class OptimizedSlidingWindowSolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        # Basic check
        if m < n:
            return False

        # Using arrays of 26 as hashmaps instead of dicts
        s1_map = [0] * 26
        s2_map = [0] * 26

        # Build the hashmap for the first string
        for i in range(n):
            s1_map[self.getIndex(s1[i])] += 1
            s2_map[self.getIndex(s2[i])] += 1

        # Maintain a count of the letters that are matching in the hashmap
        # This way once the count reaches 26 we will return True
        count = 0
        for i in range(26):
            if s1_map[i] == s2_map[i]:
                count += 1

        # Iterate over the range to add new characters in s2 map
        # And check when does the count reaches 26 meaning both hashmaps
        # Are the same
        for i in range(m - n):
            if count == 26:
                return True

            # The reason for r = s2[i + n] is because this represents the right side of the sliding window
            # And since the size of the sliding window is n, we need to add i + n to move it one step ahead each iteration
            r = self.getIndex(s2[i + n])
            l = self.getIndex(s2[i])

            # If the count of the new letter added matches the count of that letter in s1
            # Our number of matching counts increases, otherwise we decrease it
            s2_map[r] += 1
            if s2_map[r] == s1_map[r]:
                count += 1
            elif s2_map[r] == s1_map[r] + 1:
                count -= 1

            s2_map[l] -= 1
            if s2_map[l] == s1_map[l]:
                count += 1
            elif s2_map[l] == s1_map[l] - 1:
                count -= 1

        return count == 26

    def getIndex(self, char):
        return int(ord(char) - ord("a"))

    def testCheckInclusion(self, s1: str, s2: str, expected: bool):
        actual = self.checkInclusion(s1, s2)
        if actual == expected:
            print("Test Case Passed!")
        else:
            print(f"Test Case Failed! s1: {s1}, s2: {s2}, actual: {actual}, expected: {expected}")


OptimizedSlidingWindowSolution().testCheckInclusion("ab", "eidbaooo", True)
OptimizedSlidingWindowSolution().testCheckInclusion("ab", "eidboaoo", False)
OptimizedSlidingWindowSolution().testCheckInclusion("adc", "dcda", True)
