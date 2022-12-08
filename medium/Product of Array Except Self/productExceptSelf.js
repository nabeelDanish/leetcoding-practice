/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function (nums) {
  const answer = nums.length > 1 ? [1] : [0];

  // First we sweep left
  for (let i = 1; i < nums.length; ++i) {
    answer.push(answer[i - 1] * nums[i - 1]);
  }

  let right = 1;

  // Now we sweep right
  for (let i = nums.length - 1; i >= 0; --i) {
    answer[i] = right * answer[i];

    // Check for -0
    if (answer[i] == -0) answer[i] = 0;

    right = right * nums[i];
  }

  return answer;
};

const testProductExceptSelf = function (nums, output) {
  const result = productExceptSelf(nums);
  if (result == output) {
    console.log("Test Case Passed!");
  } else {
    console.log(
      `Test Case Failed: nums: ${JSON.stringify(nums)} output: ${JSON.stringify(
        output
      )} result: ${JSON.stringify(result)}`
    );
  }
};

testProductExceptSelf([1, 2, 3, 4], [24, 12, 8, 6]);
testProductExceptSelf([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]);
