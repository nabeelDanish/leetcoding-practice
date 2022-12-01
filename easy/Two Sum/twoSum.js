/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  const hashMap = {};
  const n = nums.length;

  for (let i = 0; i < n; ++i) {
    const toFind = target - nums[i];
    if (hashMap[toFind] != undefined) {
      return [i, hashMap[toFind]];
    } else {
      hashMap[nums[i]] = i;
    }
  }
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

testSum([2, 7, 11, 15], 9, [1, 0]);
testSum([3, 2, 4], 6, [2, 1]);
testSum([3, 3], 6, [1, 0]);
