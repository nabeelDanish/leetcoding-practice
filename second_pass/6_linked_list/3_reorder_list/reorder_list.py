from typing import List, Optional
from ..util import ListNode, LinkedList


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        first = head
        second = head.next
        third = head.next

        while third and third.next is not None:
            # Find the last element
            fourth = third
            while fourth.next is not None:
                third = fourth
                fourth = fourth.next

            first.next = fourth
            fourth.next = second
            third.next = None

            first = second
            second = first.next
            third = first.next

    def testReorderList(self, head: Optional[ListNode], expected: ListNode):
        self.reorderList(head)

        if not LinkedList.are_equal(head, expected):
            print(f"Test Case Failed! Linked Lists are not equal")

            print(f"actual: {LinkedList.print_list(head)}")
            print(f"expected: {LinkedList.print_list(expected)}")

        else:
            print("Test Case Passed!\n")


Solution().testReorderList(
    LinkedList.create_list([1, 2, 3, 4, 5]),
    LinkedList.create_list([1, 5, 2, 4, 3])
)
Solution().testReorderList(
    LinkedList.create_list([1, 2, 3, 4, 5, 6]),
    LinkedList.create_list([1, 6, 2, 5, 3, 4])
)
