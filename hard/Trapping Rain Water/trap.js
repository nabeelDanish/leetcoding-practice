/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function (height) {
  if (height.length === 0) return 0;

  let totalWater = 0;
  const n = height.length;

  const leftMaxHeight = Array(n);
  const rightMaxHeight = Array(n);

  for (let i = 0; i < n; ++i) {
    if (i === 0) leftMaxHeight[i] = height[i];
    else leftMaxHeight[i] = Math.max(height[i], leftMaxHeight[i - 1]);
  }

  for (let i = n - 1; i >= 0; --i) {
    if (i === n - 1) rightMaxHeight[i] = height[i];
    else rightMaxHeight[i] = Math.max(height[i], rightMaxHeight[i + 1]);
  }

  for (let i = 1; i < n; ++i) {
    totalWater += Math.min(leftMaxHeight[i], rightMaxHeight[i]) - height[i];
  }

  return totalWater;
};

const testTrap = function (height, output) {
  const result = trap(height);
  if (result === output) {
    console.log("Test Passed!");
  } else {
    console.log(
      `Test Failed!: height ${height} result ${result} output ${output}`
    );
  }
};

testTrap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6);
testTrap([4, 2, 0, 3, 2, 5], 9);
testTrap([4, 2, 3], 1);
