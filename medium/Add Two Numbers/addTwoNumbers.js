const ListNode = require("../../commons/LinkedList").ListNode;

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
const addTwoNumbers = function (l1, l2) {
  const result = new ListNode();

  let pointer1 = l1;
  let pointer2 = l2;
  let pointer3 = result;

  let carry = 0;

  while (pointer1.val != null && pointer2.val != null) {
    const val1 = pointer1.val;
    const val2 = pointer2.val;

    const sum = (val1 + val2 + carry) % 10;
    carry = Math.floor((val1 + val2 + carry) / 10);

    pointer3.val = sum;
    pointer3.next = new ListNode();

    pointer1 = pointer1.next;
    pointer2 = pointer2.next;
    pointer3 = pointer3.next;
  }

  while (pointer1.val != null) {
    const val1 = pointer1.val;
    const sum = (val1 + carry) % 10;
    carry = Math.floor((val1 + carry) / 10);

    pointer3.val = sum;
    pointer3.next = new ListNode();

    pointer1 = pointer1.next;
    pointer3 = pointer3.next;
  }

  while (pointer2.val != null) {
    const val2 = pointer2.val;
    const sum = (val2 + carry) % 10;
    carry = Math.floor((val2 + carry) / 10);

    pointer3.val = sum;
    pointer3.next = new ListNode();

    pointer2 = pointer2.next;
    pointer3 = pointer3.next;
  }

  if (carry !== 0) {
    pointer3.val = carry;
    pointer3.next = new ListNode();
  }

  return result;
};

const testAddTwoNumbers = function (l1, l2, output) {
  const result = addTwoNumbers(l1, l2);
  const l3 = new ListNode();
  l3.createList(output);

  if (l3.equal(result)) {
    console.log("Test Passed!");
  } else {
    console.log(
      `Test Failed!: l1 ${l1} l2 ${l2}, result ${result} output ${output}`
    );
  }
};

const l1 = new ListNode();
const l2 = new ListNode();

l1.createList([2, 4, 3]);
l2.createList([5, 6, 4]);

testAddTwoNumbers(l1, l2, [7, 0, 8]);

l1.clear();
l2.clear();

l1.createList([0]);
l2.createList([0]);

testAddTwoNumbers(l1, l2, [0]);

l1.clear();
l2.clear();

l1.createList([9, 9, 9, 9, 9, 9, 9]);
l2.createList([9, 9, 9, 9]);

testAddTwoNumbers(l1, l2, [8, 9, 9, 9, 0, 0, 0, 1]);
