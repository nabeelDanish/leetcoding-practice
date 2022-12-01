module.exports.ListNode = class ListNode {
  constructor(val, next) {
    this.val = val === undefined ? null : val;
    this.next = next === undefined ? null : next;
  }

  createList(list) {
    let current = this;
    for (let i = 0; i < list.length; ++i) {
      current.val = list[i];
      current.next = new ListNode();
      current = current.next;
    }
  }

  printList() {
    let current = this;
    while (current.val !== null) {
      console.log(current.val);
      current = current.next;
    }
  }

  clear() {
    this.val = null;
    this.next = null;
  }
};
