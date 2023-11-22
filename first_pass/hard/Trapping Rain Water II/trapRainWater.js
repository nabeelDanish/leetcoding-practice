/**
 * @param {number[][]} heightMap
 * @return {number}
 */
var trapRainWater = function (heightMap) {
  const m = heightMap.length;
  const n = heightMap[0].length;

  const leftMaxHeights = Array(m);
  const rightMaxHeights = Array(m);
  const upMaxHeights = Array(m);
  const downMaxHeights = Array(m);

  let totalWater = 0;

  for (let i = 0; i < m; ++i) {
    leftMaxHeights[i] = Array(n);
    rightMaxHeights[i] = Array(n);
    upMaxHeights[i] = Array(n);
    downMaxHeights[i] = Array(n);
  }

  for (let i = 0; i < m; ++i) {
    for (let j = 0; j < n; ++j) {
      if (j === 0) leftMaxHeights[i][j] = heightMap[i][j];
      else
        leftMaxHeights[i][j] = Math.max(
          heightMap[i][j],
          leftMaxHeights[i][j - 1]
        );
    }
  }

  for (let i = 0; i < m; ++i) {
    for (let j = n - 1; j >= 0; --j) {
      if (j === n - 1) rightMaxHeights[i][j] = heightMap[i][j];
      else
        rightMaxHeights[i][j] = Math.max(
          heightMap[i][j],
          rightMaxHeights[i][j + 1]
        );
    }
  }

  for (let j = 0; j < n; ++j) {
    for (let i = 0; i < m; ++i) {
      if (i === 0) upMaxHeights[i][j] = heightMap[i][j];
      else
        upMaxHeights[i][j] = Math.max(heightMap[i][j], upMaxHeights[i - 1][j]);
    }
  }

  for (let j = 0; j < n; ++j) {
    for (let i = m - 1; i >= 0; --i) {
      if (i === m - 1) downMaxHeights[i][j] = heightMap[i][j];
      else
        downMaxHeights[i][j] = Math.max(
          heightMap[i][j],
          downMaxHeights[i + 1][j]
        );
    }
  }

  for (let i = 1; i < m - 1; ++i) {
    for (let j = 1; j < n - 1; ++j) {
      totalWater +=
        Math.min(
          Math.min(leftMaxHeights[i][j], rightMaxHeights[i][j]),
          Math.min(upMaxHeights[i][j], downMaxHeights[i][j])
        ) - heightMap[i][j];
    }
  }

  return totalWater;
};

const testTrapRainWater = function (heightMap, output) {
  const result = trapRainWater(heightMap);
  if (result === output) {
    console.log("Test Passed!");
  } else {
    console.log(
      `Test Failed!: height ${heightMap} result ${result} output ${output}`
    );
  }
};

testTrapRainWater(
  [
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1],
  ],
  4
);
testTrapRainWater(
  [
    [3, 3, 3, 3, 3],
    [3, 2, 2, 2, 3],
    [3, 2, 1, 2, 3],
    [3, 2, 2, 2, 3],
    [3, 3, 3, 3, 3],
  ],
  10
);
testTrapRainWater(
  [
    [12, 13, 1, 12],
    [13, 4, 13, 12],
    [13, 8, 10, 12],
    [12, 13, 12, 12],
    [13, 13, 13, 13],
  ],
  14
);
