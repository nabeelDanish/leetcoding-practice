/**
 * @param {number[]} nums
 * @return {number[]}
 */
var buildArray = function (nums) {
    return nums.map((num) => nums[num])
};

const testBuildArray = function (nums, expected) {
    const result = buildArray(nums)
    if (result == expected) {
        console.log("Test Case Passed!")
    } else {
        console.log(`Test Case Failed: nums = ${nums}, result = ${result}, expected = ${expected}`)
    }
}

testBuildArray([0, 2, 1, 5, 3, 4], [0, 1, 2, 4, 5, 3])
testBuildArray([5, 0, 1, 2, 3, 4], [4, 5, 0, 1, 2, 3])