/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
  const numCounts = {};
  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    if (numCounts[num] != null) {
      numCounts[num] += 1;
    } else {
      numCounts[num] = 1;
    }
  }

  // Filling Count Nums
  const countNums = [];
  for (let i = 0; i <= nums.length; ++i) {
    countNums.push([]);
  }

  // Inverting Counts and Nums
  const keys = Object.keys(numCounts);
  for (let i = 0; i < keys.length; ++i) {
    const key = keys[i];
    const value = numCounts[key];

    countNums[value]?.push(Number(key));
  }

  // Iterating over the counts in reverse order to find
  // Top k
  let result = [];
  for (let i = nums.length; i >= 0; --i) {
    if (countNums[i].length > 0) {
      result = result.concat(countNums[i]);
      if (result.length >= k) {
        break;
      }
    }
  }

  return result;
};

const testTopKFrequent = function (nums, k, output) {
  const result = topKFrequent(nums, k);
  if (result == output) {
    console.log("Test Case Passed!");
  } else {
    console.log(
      `Test Case Failed: nums: ${JSON.stringify(
        nums
      )} k: ${k} output: ${JSON.stringify(output)} result: ${JSON.stringify(
        result
      )}`
    );
  }
};

testTopKFrequent([1, 1, 1, 2, 2, 3], 2, [1, 2]);
testTopKFrequent([1], 1, [1]);
testTopKFrequent([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]);
testTopKFrequent([1, 5, 9, 1, 3, 2, 9, 5, 5], 3, [5, 9, 1]);
