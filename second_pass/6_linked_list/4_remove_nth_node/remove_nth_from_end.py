from typing import Optional
from ..util import ListNode, LinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = head
        end = head

        steps = 0
        for _ in range(n):
            if not end:
                break
            end = end.next
            steps += 1

        if not end:
            while steps <= n and head:
                head = head.next
                steps += 1

        else:
            while end.next:
                end = end.next
                start = start.next
            
            to_remove = start.next
            start.next = to_remove.next
        
        return head


    def testRemoveNthFromEnd(self, head: Optional[ListNode], n: int, expected: Optional[ListNode]):
        actual = self.removeNthFromEnd(head, n)

        if not LinkedList.are_equal(actual, expected):
            print(f"\nTest Case Failed! Linked Lists are not equal")
            print(f"actual: ")
            LinkedList.print_list(head)
            print(f"expected: ")
            LinkedList.print_list(expected)

        else:
            print("Test Case Passed!\n")


Solution().testRemoveNthFromEnd(
    LinkedList.create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]),
    3,
    LinkedList.create_list([1, 2, 3, 4, 5, 6, 8, 9])
)
Solution().testRemoveNthFromEnd(
    LinkedList.create_list([1, 2]),
    1,
    LinkedList.create_list([1])
)
Solution().testRemoveNthFromEnd(
    LinkedList.create_list([1, 2]),
    1,
    LinkedList.create_list([1])
)
Solution().testRemoveNthFromEnd(
    LinkedList.create_list([1, 2, 3]),
    3,
    LinkedList.create_list([2, 3])
)
Solution().testRemoveNthFromEnd(
    LinkedList.create_list([1]),
    1,
    None
)