/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const map = {};
    for (let i = 0; i < nums.length; ++i) {
        if (map[nums[i]] != null) {
            return true;
        }
        map[nums[i]] = i;
    }
    return false;
};

const testContainsDuplicate = function(nums, expected) {
    const result = containsDuplicate(nums);
    if (result == expected) {
        console.log("Test Case Passed!");
    } else {
        console.log(
            `Test Case Failed: nums: ${nums} expected: ${expected} result: ${result}`
        );
    }
}

testContainsDuplicate([1,2,3,1], true);
testContainsDuplicate([1,2,3,4], false);
testContainsDuplicate([1,1,1,3,3,4,3,2,4,2], true);