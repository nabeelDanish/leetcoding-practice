/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  if (s.length <= 1) return s.length;

  const letterCount = {};
  let start = 0;
  let end = 0;

  let maxLength = 0;

  while (end < s.length) {
    const letter = s[end];
    if (letterCount[letter] != null && letterCount[letter]) {
      maxLength = Math.max(maxLength, end - start);
      letterCount[s[start]] = false;
      ++start;
    } else {
      letterCount[letter] = true;
      ++end;
    }
  }

  return Math.max(maxLength, end - start);
};

const testLengthOfLongestSubstring = function (s, output) {
  const result = lengthOfLongestSubstring(s);
  if (result === output) {
    console.log("Test Case Passed!");
  } else {
    console.log(
      `Test Case Failed: s: ${s} output: ${output} result: ${result}`
    );
  }
};

testLengthOfLongestSubstring("abcabcbb", 3);
testLengthOfLongestSubstring("bbbbb", 1);
testLengthOfLongestSubstring("pwwkew", 3);
testLengthOfLongestSubstring(" ", 1);
testLengthOfLongestSubstring("au", 2);
