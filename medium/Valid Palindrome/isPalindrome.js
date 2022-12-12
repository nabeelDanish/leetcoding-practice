/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  // Preprocessing the string
  const sanitized = s.replace(/[\W|_]/g, "").toLowerCase();

  // Finding the center
  const n = sanitized.length;
  const center = Math.floor(n / 2);

  // Using two pointers
  let i = 0;
  let j = n - 1;

  for (i = 0; i < center; i++) {
    const a = sanitized[i];
    const b = sanitized[j];

    if (a != b) {
      return false;
    }

    --j;
  }

  return true;
};

const testIsPalindrome = function (s, output) {
  const result = isPalindrome(s);
  if (result == output) {
    console.log("Test Case Passed!");
  } else {
    console.log(
      `Test Case Failed: s: ${s} output: ${output} result: ${result}`
    );
  }
};

testIsPalindrome("A man, a plan, a canal: Panama", true);
testIsPalindrome("race a car", false);
testIsPalindrome(" ", true);
testIsPalindrome("ab_a", true);
testIsPalindrome("0P", false);
