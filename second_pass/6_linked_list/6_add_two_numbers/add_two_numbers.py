from typing import Optional
from ..util import ListNode, LinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = l1
        s2 = l2

        val = (s1.val + s2.val) % 10
        carry = (s1.val + s2.val) // 10

        new_list = ListNode(val=val)
        s3 = new_list
        s1 = s1.next
        s2 = s2.next

        while s1 and s2:
            val = (s1.val + s2.val + carry) % 10
            carry = (s1.val + s2.val + carry) // 10
            s3.next = ListNode(val)

            s3 = s3.next
            s1 = s1.next
            s2 = s2.next

        while s1:
            val = (s1.val + carry) % 10
            carry = (s1.val + carry) // 10
            s3.next = ListNode(val)

            s3 = s3.next
            s1 = s1.next

        while s2:
            val = (s2.val + carry) % 10
            carry = (s2.val + carry) // 10
            s3.next = ListNode(val)

            s3 = s3.next
            s2 = s2.next

        if carry:
            s3.next = ListNode(carry)

        return new_list

    def testAddTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], expected: Optional[ListNode]):
        actual = self.addTwoNumbers(l1, l2)

        if not LinkedList.are_equal(actual, expected):
            print(f"\nTest Case Failed! Linked Lists are not equal")
            print(f"actual: ")
            LinkedList.print_list(actual)
            print(f"expected: ")
            LinkedList.print_list(expected)

        else:
            print("Test Case Passed!\n")


Solution().testAddTwoNumbers(
    LinkedList.create_list([2, 4, 3]),
    LinkedList.create_list([5, 6, 4]),
    LinkedList.create_list([7, 0, 8]),
)
Solution().testAddTwoNumbers(
    LinkedList.create_list([0]),
    LinkedList.create_list([0]),
    LinkedList.create_list([0]),
)
Solution().testAddTwoNumbers(
    LinkedList.create_list([9, 9, 9, 9, 9, 9, 9]),
    LinkedList.create_list([9, 9, 9, 9]),
    LinkedList.create_list([8, 9, 9, 9, 0, 0, 0, 1]),
)
