/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function (nums, k) {
    const maxWindow = [];
    const n = nums.length;

    // Initial Fixed sized window
    let left = 0;
    let right = k - 1;

    // Initial Max calculation
    const slice = nums.slice(left, right + 1);
    let previousMax = Math.max(...slice);
    let previousMaxIndex = slice.indexOf(previousMax);
    maxWindow.push(previousMax);

    right += 1;
    left += 1;

    while (right < n) {
        // We first check if the previous max number is still
        // In the array
        const isStillIn = ((left <= previousMaxIndex) && (previousMaxIndex <= right))

        // If still in we only compute for the new number
        if (isStillIn) {
            if (previousMax > nums[right]) {
                maxWindow.push(previousMax);
            } else {
                previousMax = nums[right];
                previousMaxIndex = right;
                maxWindow.push(previousMax);
            }
        } else {
            // Otherwise compute the calculation again
            const slice = nums.slice(left, right + 1);
            previousMax = Math.max(...slice);
            previousMaxIndex = slice.indexOf(previousMax);
            maxWindow.push(previousMax);
        }

        right += 1;
        left += 1;
    }

    return maxWindow;
};

const testMaxSlidingWindow = function (nums, k, output) {

}