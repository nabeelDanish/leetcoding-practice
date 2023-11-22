/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (numbers, target) {
  let start = 0;
  let end = numbers.length - 1;
  let sum = numbers[start] + numbers[end];

  while (sum != target) {
    if (sum > target) end -= 1;
    else start += 1;

    sum = numbers[start] + numbers[end];
  }

  return [start + 1, end + 1];
};

const testSum = function (nums, target, output) {
  const result = twoSum(nums, target);
  if (result == output) {
    console.log("Test Case Passed!");
  } else {
    console.log(
      `Test Case Failed: nums: ${nums} target: ${target} output: ${output} result: ${result}`
    );
  }
};

testSum([2, 7, 11, 15], 9, [1, 2]);
testSum([2, 3, 4], 6, [1, 3]);
testSum([-1, 0], -1, [1, 2]);
testSum([5, 25, 75], 100, [2, 3]);
testSum([3, 24, 50, 79, 88, 150, 345], 200, [3, 6]);
