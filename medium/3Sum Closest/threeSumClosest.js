/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
    nums.sort((a, b) => { return a - b })

    let closestSum = Number.MAX_VALUE;

    for (let i = 0; i < nums.length; ++i) {
        let first = nums[i];
        let toFind = target - first

        let start = i + 1;
        let end = nums.length - 1;

        while (start < end) {
            sum = first + nums[start] + nums[end];
            closestSum = Math.abs(closestSum - target) < Math.abs(sum - target) ? closestSum : sum;

            if (nums[start] + nums[end] > toFind) {
                end -= 1;
            } else {
                start += 1;
            }
        }
    }

    return closestSum
};

const testThreeSumClosest = function (nums, target, expected) {
    const result = threeSumClosest(nums, target);
    if (result == expected) {
        console.log("Test Case Passed!");
    } else {
        console.log(`Test Case Failed! nums: ${nums} target: ${target} result: ${result} expected: ${expected}`)
    }
}

testThreeSumClosest([-1, 2, 1, -4], 1, 2)
testThreeSumClosest([0, 0, 0], 1, 0)