/**
 * @param {number[]} nums
 * @param {number} indexDiff
 * @param {number} valueDiff
 * @return {boolean}
 */
var containsNearbyAlmostDuplicate = function(nums, indexDiff, valueDiff) {
    const map = {};
    const k = indexDiff;

    for (let i = 0; i < nums.length; i++) {
        const element = nums[i];

        let diff1 = Math.abs(element - valueDiff);
        let diff2 = Math.abs(element + valueDiff);

        let decrement = valueDiff;

        while (decrement >= 0) {
            if (map[diff1] != null) {
                const j = map[diff1];
                if (Math.abs(i - j) <= k) {
                    return true;
                }
            }

            if (map[diff2] != null) {
                const j = map[diff2];
                if (Math.abs(i - j) <= k) {
                    return true;
                }
            }

            --decrement;

            diff1 = Math.abs(element - decrement);
            diff2 = Math.abs(element + decrement);
        }

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

const testContainsNearbyAlmostDuplicate = function(nums, indexDiff, valueDiff, expected) {
    const output = containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff);
    if (output == expected) {
        console.log("Test Case Passed!");
    } else {
        console.log(
          `Test Case Failed: nums: ${nums} output: ${output} expected: ${expected}`
        );
    }
}

testContainsNearbyAlmostDuplicate([1,2,3,1], 3, 0, true);
testContainsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3, false);
testContainsNearbyAlmostDuplicate([8,7,15,1,6,1,9,15], 1, 3, true);
testContainsNearbyAlmostDuplicate([-1,-1], 1, 0, true);