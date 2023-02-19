/**
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
 * determine if the input string is valid.
 * 
 * An input string is valid if:
 * 
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * Every close bracket has a corresponding open bracket of the same type.
 */

/**
 * @param {string} s
 * @return {boolean}
 */
const isValid = function(s) {
    const stack = [];
    const n = s.length;

    for (let i = 0; i < n; ++i) {
        const parenthesis = s[i];

        if (parenthesis == ")" || parenthesis == "]" || parenthesis == "}") {
            const other = stack.pop();
            switch (parenthesis) {
                case ")": 
                    if (other != "(") return false;
                    break;
                case "}": 
                    if (other != "{") return false;
                    break;
                case "]": 
                    if (other != "[") return false;
                    break;
                default:
                    return false;
            }
        } else {
            stack.push(parenthesis);
        }
    }

    return stack.length === 0
};

const testIsValid = (s, output) => {
    const result = isValid(s);
    if (result === output) {
        console.log("Test Case Passed!");
    } else {
        console.log(
            `Test Case Failed: s: ${s} output: ${output} result: ${result}`
        );
    }
}

testIsValid("()", true);
testIsValid("()[]{}", true);
testIsValid("(]", false)