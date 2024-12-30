from typing import Optional, List
from ..util import ListNode, LinkedList

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        finalList = None
        while True:
            minVal = float("inf")
            minIndex = -1
            for i, l in enumerate(lists):
                if l and l.val < minVal:
                    minVal = l.val
                    minIndex = i

            if minIndex == -1:
                break

            if not finalList:
                finalList = ListNode(minVal)
                finalListTail = finalList
            else:
                finalListTail.next = ListNode(minVal)
                finalListTail = finalListTail.next

            lists[minIndex] = lists[minIndex].next

        return finalList

    def testMergeKLists(self, lists: List[Optional[ListNode]], expected: Optional[ListNode]):
        actual = self.mergeKLists(lists)

        if not LinkedList.are_equal(actual, expected):
            print(f"\nTest Case Failed! Linked Lists are not equal")
            print(f"actual: ")
            LinkedList.print_list(actual)
            print(f"expected: ")
            LinkedList.print_list(expected)
        else:
            print("Test Case Passed.")

Solution().testMergeKLists(
    [
        LinkedList.create_list([1, 4, 5]),
        LinkedList.create_list([1, 4, 5]),
        LinkedList.create_list([2, 6]),
    ],
    LinkedList.create_list([1, 1, 2, 4, 4, 5, 5, 6])
)
Solution().testMergeKLists(
    [],
    None
)