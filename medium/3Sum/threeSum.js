/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function (nums) {
  const sorted = nums;

  // First Sort so that we can use it like Two Sum II Problem
  sorted.sort();

  const n = sorted.length;
  const result = [];

  console.log("sorted :>> ", sorted);

  // No we iterate over the array and
  // Use the current element as the target sum
  // So for [1, 2, 3], target sum = -1. we need to find 2 numbers that add to -1
  // Lets call those x and y, then our triplet will be [1, x, y]
  for (let i = 0; i < n - 2; ++i) {
    // Ensure that we are looping over the duplicates
    if (i > 0 && sorted[i] == sorted[i - 1]) continue;

    // Start is going to be 1 + current since we are sweeping right
    // we do not want to consider numbers that we have already traversed
    let start = i + 1;
    let end = n - 1;
    const target = 0 - sorted[i];

    // Now we perform the Two Sum II Thing
    while (start < end) {
      const sum = sorted[start] + sorted[end];

      if (sum == target) {
        result.push([sorted[i], sorted[start], sorted[end]]);

        // We do need to move the pointer, since we have to find other pairs
        // So we loop over the duplicates of this number
        while (sorted[start] == sorted[start + 1] && start < end) start += 1;
        while (sorted[end] == sorted[end - 1] && start < end) end -= 1;

        // Final pointer movement
        start += 1;
        end -= 1;
      } else if (sum < target) start += 1;
      else end -= 1;
    }
  }

  return result;
};

const equal = function (result, output) {
  return (
    JSON.stringify(result).split("").sort().join("") ==
    JSON.stringify(output).split("").sort().join("")
  );
};

const testThreeSum = function (nums, output) {
  const result = threeSum(nums);
  if (equal(result, output)) {
    console.log("Test Case Passed!");
  } else {
    console.log(
      `Test Case Failed: nums: ${JSON.stringify(nums)} output: ${JSON.stringify(
        output
      )} result: ${JSON.stringify(result)}`
    );
  }
};

testThreeSum(
  [-1, 0, 1, 2, -1, -4],
  [
    [-1, -1, 2],
    [-1, 0, 1],
  ]
);
testThreeSum([0, 1, 1], []);
testThreeSum([0, 0, 0], [[0, 0, 0]]);
testThreeSum([0, 0, 0, 0], [[0, 0, 0]]);
testThreeSum(
  [-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4],
  [
    [-4, 0, 4],
    [-4, 1, 3],
    [-3, -1, 4],
    [-3, 0, 3],
    [-3, 1, 2],
    [-2, -1, 3],
    [-2, 0, 2],
    [-1, -1, 2],
    [-1, 0, 1],
  ]
);
