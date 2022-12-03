/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const map = {};

    for (let i = 0; i < nums.length; i++) {
        const element = nums[i];
        if (map[element] != null) {
            const j = map[element];
            if (Math.abs(i - j) <= k) {
                return true;
            }
        }
        map[element] = i;
    }

    return false;
};

const testContainsNearbyDuplicate = function(nums, k, expected) {
    const output = containsNearbyDuplicate(nums, k);
    if (output == expected) {
        console.log("Test Case Passed!");
    } else {
        console.log(
          `Test Case Failed: nums: ${nums} k: ${k} output: ${output} expected: ${expected}`
        );
    }
}

testContainsNearbyDuplicate([1,2,3,1], 3, true)
testContainsNearbyDuplicate([1,0,1,1], 1, true)
testContainsNearbyDuplicate([1,2,3,1,2,3], 2, false)