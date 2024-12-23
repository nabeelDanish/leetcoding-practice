from typing import List


class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    @classmethod
    def create_list(cls, list: List[int]):
        if not list:
            return None

        head = ListNode(val=list[0])
        next = head
        n = len(list)
        for i in range(1, n):
            next.next = ListNode(val=list[i])
            next = next.next

        return head

    @classmethod
    def print_list(cls, head: ListNode):
        if not head:
            return

        next = head
        while next:
            print(next.val, end=", ")
            next = next.next
        
        print(end="\n")

    @classmethod
    def are_equal(cls, list1: ListNode, list2: ListNode):        
        first = list1
        second = list2

        while first and second:
            if not first.val == second.val:
                return False
            first = first.next
            second = second.next

        return not(first or second)
    
    @classmethod
    def add_cycle(cls, head: ListNode, pos: int):
        if pos < 0:
            return head
        
        cycle_start = None
        current = head
        index = 0

        while current.next:
            if index == pos:
                cycle_start = current
            current = current.next
            index += 1

        current.next = cycle_start
        return head