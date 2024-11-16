from typing import Optional
from ..util import LinkedList, ListNode

# Definition for singly-linked list.


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        
        first = list1
        second = list2
        new_list = ListNode()
        start = None

        while first and second:
            new_list.next = ListNode()
            new_list = new_list.next
            
            if not start:
                start = new_list
            
            if first.val < second.val:
                new_list.val = first.val
                first = first.next
            else:
                new_list.val = second.val
                second = second.next

        while first:
            new_list.next = ListNode()
            new_list = new_list.next

            if not start:
                start = new_list

            new_list.val = first.val
            first = first.next

        while second:
            new_list.next = ListNode()
            new_list = new_list.next

            if not start:
                start = new_list

            new_list.val = second.val
            second = second.next

        return start

    def testMergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode], expected: Optional[ListNode]):
        actual = self.mergeTwoLists(list1, list2)
        if not LinkedList.are_equal(actual, expected):
            print(f"Test Case Failed! Linked Lists are not equal")

            print(f"actual: {LinkedList.print_list(actual)}")
            print(f"expected: {LinkedList.print_list(expected)}")

        else:
            print("Test Case Passed!\n")


Solution().testMergeTwoLists(
    LinkedList.create_list([1, 2, 4]),
    LinkedList.create_list([1, 3, 4]),
    LinkedList.create_list([1, 1, 2, 3, 4, 4])
)

Solution().testMergeTwoLists(
    LinkedList.create_list([]),
    LinkedList.create_list([]),
    LinkedList.create_list([])
)

Solution().testMergeTwoLists(
    LinkedList.create_list([]),
    LinkedList.create_list([0]),
    LinkedList.create_list([0])
)
