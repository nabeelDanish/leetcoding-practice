/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function (prices) {
  if (prices.length < 1) {
    return 0;
  }

  let broughtFor = prices[0];
  let maxProfit = 0;

  for (let i = 1; i < prices.length; ++i) {
    if (prices[i] < broughtFor) {
      broughtFor = prices[i];
    } else {
      maxProfit = Math.max(maxProfit, prices[i] - broughtFor);
    }
  }

  return maxProfit;
};

const testMaxProfit = function (prices, expected) {
  const result = maxProfit(prices);
  if (result == expected) {
    console.log("Test Case Passed!");
  } else {
    console.log(
      `Test Case Failed: prices: ${prices} expected: ${expected} result: ${result}`
    );
  }
};

testMaxProfit([7, 1, 5, 3, 6, 4], 5);
testMaxProfit([7, 6, 4, 3, 1], 0);
testMaxProfit([1], 0);
