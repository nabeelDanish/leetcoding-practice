/**
 * @param {string[]} operations
 * @return {number}
 */
var finalValueAfterOperations = function (operations) {
    let result = 0;
    for (let i = 0; i < operations.length; ++i) {
        result += (operations[i] == "++X" || operations[i] == "X++") ? 1 : -1
    }
    return result
};

const testFinalValueAfterOperations = function (operations, expected) {
    const result = finalValueAfterOperations(operations);
    if (result === expected) {
        console.log("Test Case Passed!")
    } else {
        console.log(`Test Case Failed! operations: ${operations} result: ${result} expected: ${expected}`)
    }
}

testFinalValueAfterOperations(["--X", "X++", "X++"], 1)
testFinalValueAfterOperations(["++X", "++X", "X++"], 3)
testFinalValueAfterOperations(["X++", "++X", "--X", "X--"], 0)