const { compareArrays } = require("../../commons/util");

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getConcatenation = function (nums) {
    const result = Array(nums.length * 2)

    nums.forEach((num, index) => {
        result[index] = num;
        result[index + nums.length] = num
    })

    return result
};

const testGetConcatenation = function (nums, expected) {
    const result = getConcatenation(nums)
    if (compareArrays(result, expected)) {
        console.log("Test Case Passed!")
    } else {
        console.log(`Test Case Failed: nums = ${nums}, result = ${result}, expected = ${expected}`)
    }
}

testGetConcatenation([1, 2, 1], [1, 2, 1, 1, 2, 1])
testGetConcatenation([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1])
