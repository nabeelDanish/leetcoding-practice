var MinStack = function() {
    this.stack = [];
    // Stack will hold a tuple of [element, minElement]
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    const n = this.stack.length;
    if (n > 0) {
        const lastTuple = this.stack[n - 1];
        const lastMin = lastTuple[1];

        this.stack.push([val, Math.min(lastMin, val)]);
    } else {
        this.stack.push([val, val]);
    }
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.stack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    const n = this.stack.length;
    if (n > 0) return this.stack[n - 1][0];
    else return null;
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    const n = this.stack.length;
    if (n > 0) {
        const lastTuple = this.stack[n - 1];
        return lastTuple[1];
    } else return null
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */

const testMinStack = () => {
    const obj = new MinStack();
    obj.push(-2);
    obj.push(0);
    obj.push(-3);

    let min = obj.getMin();
    if (min !== -3) {
        console.log("getMin() -> -3 test case failed!");
    }

    obj.pop();

    let top = obj.top();
    if (top !== 0) {
        console.log("top() -> 0 test case failed!");
    }

    min = obj.getMin();
    if (min !== -2) {
        console.log("getMin() -> -2 test case failed!");
    }

    console.log("Test Case Passed!");
}

testMinStack();