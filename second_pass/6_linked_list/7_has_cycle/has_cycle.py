from typing import Optional
from ..util import ListNode, LinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        if first.next is None:
            return False

        second = first
        first = first.next

        while first:
            if not first.next:
                return False

            if first == second:
                return True

            first = first.next

            if not first:
                return False

            first = first.next
            second = second.next

    def testHasCycle(self, head: Optional[ListNode], expected: bool):
        actual = self.hasCycle(head)

        if not actual == expected:
            print(f"\nTest Case Failed! Linked Lists are not equal")
            print(f"actual: {actual}")
            print(f"expected: {expected}")
        else:
            print("Test Case Passed!\n")


Solution().testHasCycle(
    LinkedList.add_cycle(LinkedList.create_list([3, 2, 0, -4]), 1), True
)
Solution().testHasCycle(
    LinkedList.add_cycle(LinkedList.create_list([1, 2]), 0), True
)
Solution().testHasCycle(
    LinkedList.add_cycle(LinkedList.create_list([1]), -1), False
)
Solution().testHasCycle(
    LinkedList.add_cycle(LinkedList.create_list([-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21, 23, -21, 5]), -1), False
)
