const { compareArrays } = require("../../commons/util")

/**
 * @param {number[]} nums
 * @param {number} n
 * @return {number[]}
 */
var shuffle = function (nums, n) {
    const result = Array(nums.length)

    let i = 0;
    let j = n;
    let counter = 0

    while (counter < nums.length) {
        if (counter % 2 === 0) {
            result[counter] = nums[i]
            i += 1
        } else {
            result[counter] = nums[j]
            j += 1
        }
        counter += 1
    }

    return result
};

const testShuffle = function (nums, n, expected) {
    const result = shuffle(nums, n);
    if (compareArrays(result, expected)) {
        console.log("Test Case Passed!")
    } else {
        console.log(`Test Case Failed: nums = ${nums}, result = ${result}, expected = ${expected}`)
    }
}

testShuffle([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7])
testShuffle([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1])
testShuffle([1, 1, 2, 2], 2, [1, 2, 1, 2])