const evalaute = function (a, b, operator) {
    switch (operator) {
        case "+": return a + b;
        case "-": return b - a;
        case "/": return Math.trunc(b / a);
        case "*": return a * b;
        default: throw new Error("Invalid Operator");
    }
}

/**
 * @param {string[]} tokens
 * @return {number}
 */
var evalRPN = function (tokens) {
    const stack = [];

    for (let i = 0; i < tokens.length; ++i) {
        if (!isNaN(tokens[i])) {
            stack.push(Number.parseInt(tokens[i]));
        } else {
            const operator = tokens[i];
            const a = stack.pop();
            const b = stack.pop();

            const c = evalaute(a, b, operator);

            stack.push(c);
        }
    }

    return stack.pop();
};

const testEvalRPNS = function (tokens, expected) {
    const result = evalRPN(tokens);
    if (result === expected) {
        console.log("Test Case Passed!")
    } else {
        console.log(`Test Case Failed: tokens: ${tokens}, result: ${result}, expected: ${expected}`)
    }
}

testEvalRPNS(["2", "1", "+", "3", "*"], 9)
testEvalRPNS(["4", "13", "5", "/", "+"], 6)
testEvalRPNS(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22)
testEvalRPNS(["4", "3", "-"], 1)