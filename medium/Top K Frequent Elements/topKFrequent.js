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
  const arrCounts = Object.keys(numCounts).map((key) => {
    return { key: Number(key), value: numCounts[key] };
  });

  const sortedCounts = arrCounts.sort((a, b) => {
    return a.value > b.value ? -1 : 1;
  });

  const result = [];

  for (let i = 0; i < k; i++) {
    result.push(sortedCounts[i].key);
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
