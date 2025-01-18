from typing import Optional, List
from ..util import ListNode, LinkedList

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        heads = []
        first = head
        second = head

        stepped = 1

        # break the linked list down into k groups
        while second is not None:
            if stepped == k:
                heads.append(first)
                first = second.next
                second.next = None
                second = first
                stepped = 1
            else:
                second = second.next
                stepped += 1

        # last one that didn't fit the k
        heads.append(first)

        # if the last one didn't fit the k we don't reverse it
        to_reverse_last = stepped == (k + 1)

        # reverse each group
        reversed_pointers = []
        n = len(heads)

        for i, head_pointer in enumerate(heads):
            if i == n - 1:
                if to_reverse_last:
                    reversed_pointers.append(self.reverseList(head_pointer))
                else:
                    reversed_pointers.append(head_pointer)
            else:
                reversed_pointers.append(self.reverseList(head_pointer))

        # string the heads together
        for i in range(0, n - 1):
            # find the last pointer for this list
            last_pointer = reversed_pointers[i]
            while last_pointer.next is not None:
                last_pointer = last_pointer.next

            # string the last pointer of the previous head to the head of the next reversed chunk
            last_pointer.next = reversed_pointers[i + 1]

        # return the first head pointer
        return reversed_pointers[0]

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        if head.next is None:
            return head

        first_pointer = head
        second_pointer = head.next

        first_pointer.next = None

        while second_pointer.next:
            temp_pointer = second_pointer.next
            second_pointer.next = first_pointer

            first_pointer = second_pointer
            second_pointer = temp_pointer

        second_pointer.next = first_pointer
        return second_pointer

    def testReverseKGroup(self, head: Optional[ListNode], k: int, expected: Optional[ListNode]):
        actual = self.reverseKGroup(head, k)

        if not LinkedList.are_equal(actual, expected):
            print(f"\nTest Case Failed! Linked Lists are not equal")
            print(f"actual: ")
            LinkedList.print_list(actual)
            print(f"expected: ")
            LinkedList.print_list(expected)
        else:
            print("Test Case Passed.")


Solution().testReverseKGroup(
    LinkedList.create_list([1, 2, 3, 4, 5]), 2,
    LinkedList.create_list([2, 1, 4, 3, 5])
)
Solution().testReverseKGroup(
    LinkedList.create_list([1, 2, 3, 4, 5]), 3,
    LinkedList.create_list([3, 2, 1, 4, 5])
)
