from typing import Optional, List
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
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

    def testReverseList(self, initial: List[int], expected: List[int]):
        if not initial:
            return print("Test Case Passed!")
        
        head = ListNode(val=initial[0])
        next = head
        for i in range(1, len(initial)):
            next.next = ListNode(val=initial[i])
            next = next.next

        actual = self.reverseList(head)
        for value in expected:
            assert actual, f"pointer out of range!!!"
            assert actual.val == value, f"value incorrect for {actual.value} - {actual} vs {value}"
            actual = actual.next
        
        print("Test Case Passed!")


Solution().testReverseList([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
Solution().testReverseList([1, 2], [2, 1])
Solution().testReverseList([], [])
