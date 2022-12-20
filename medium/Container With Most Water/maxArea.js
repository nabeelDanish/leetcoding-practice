/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
  let maxArea = 0;
  const n = height.length;

  let left = 0;
  let right = n - 1;

  while (left < right) {
    const line1 = height[left];
    const line2 = height[right];

    const area = Math.min(line1, line2) * Math.abs(left - right);
    maxArea = Math.max(area, maxArea);

    if (line1 < line2) left += 1;
    else right -= 1;
  }

  return maxArea;
};

const testMaxArea = function (height, output) {
  const result = maxArea(height);
  if (result === output) {
    console.log("Test Passed!");
  } else {
    console.log(
      `Test Failed!: height ${height} result ${result} output ${output}`
    );
  }
};

testMaxArea([1, 8, 6, 2, 5, 4, 8, 3, 7], 49);
testMaxArea([1, 1], 1);
