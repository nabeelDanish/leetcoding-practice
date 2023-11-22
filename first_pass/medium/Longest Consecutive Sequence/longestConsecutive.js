/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const sequenceMap = {};
  let longestSequence = 0;

  // Sending everything to a hashmap
  for (let i = 0; i < nums.length; i++) {
    const element = nums[i];
    if (sequenceMap[element] == null) {
      sequenceMap[element] = element;
    }
  }

  // Iterating over the hashmap
  const numbers = Object.keys(sequenceMap);
  for (let i = 0; i < numbers.length; ++i) {
    const num = Number(numbers[i]);

    // Check if the starting number
    // If yes then we count forward
    const previousNumber = num - 1;
    if (sequenceMap[previousNumber] == null) {
      let sequenceLength = 1;
      let nextNum = num + 1;

      // Finding the end of the sequnce
      while (sequenceMap[nextNum] != null) {
        ++sequenceLength;
        ++nextNum;
      }

      // Getting the max
      longestSequence = Math.max(longestSequence, sequenceLength);
    }
  }

  return longestSequence;
};

const testLongestConsecutive = function (nums, output) {
  const result = longestConsecutive(nums);
  if (result == output) {
    console.log("Test Case Passed!");
  } else {
    console.log(
      `Test Case Failed: nums: ${nums} output: ${output} result: ${result}`
    );
  }
};

testLongestConsecutive([], 0);
testLongestConsecutive([1], 1);
testLongestConsecutive([100, 4, 200, 1, 3, 2], 4);
testLongestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9);
