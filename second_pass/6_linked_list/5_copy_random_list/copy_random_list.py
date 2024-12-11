from typing import Optional, List
from venv import create
# Definition for a Node.


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return

        copied_head = Node(head.val)
        visited = {}
        if head.random:
            random_node = head.random

            # Edge case: Check if the random node is itself
            if random_node is head:
                copied_head.random = copied_head
            else:
                copied_head.random = Node(random_node.val)

            random_node = head.random
            visited[random_node] = copied_head.random

        visited[head] = copied_head

        # Initialize our pointers from the start
        s1 = head
        s2 = copied_head

        # Repeating steps for all the next nodes
        while s1.next:
            s1 = s1.next

            # Check if the node is visited or not
            if visited.get(s1, None):
                s2.next = visited[s1]
                s2 = s2.next
            else:
                # If the node is not visited than we need to create a new one in the copied
                s2.next = Node(s1.val)
                s2 = s2.next

                # Mark s1 visited
                visited[s1] = s2

            # Now we copy the random by first checking if the random exists
            if s1.random:
                # If the random node is already visited we need to link to that one
                if visited.get(s1.random, None):
                    s2.random = visited[s1.random]
                else:
                    # Otherwise we create a new node
                    s2.random = Node(s1.random.val)
                    visited[s1.random] = s2.random

        return copied_head

    def testCopyRandomList(self, head: Optional[Node], expected: Optional[Node]):
        actual = self.copyRandomList(head)

        print("actual:")
        print_node_list(actual)
        print("\nexpected:")
        print_node_list(expected)


def print_node_list(head: Node):
    start = head
    list = []
    random_list = []

    while start:
        list.append(start.val)

        if start.random:
            random_list.append(start.random.val)
        else:
            random_list.append(None)

        start = start.next

    num_strs = [str(num) for num in list]
    random_strs = [str(num) if num else "-" for num in random_list]

    first_row = " -> ".join(num_strs)
    second_row = "    ".join("|".center(len(num)) for num in num_strs)
    third_row = "    ".join("V".center(len(num)) for num in num_strs)
    fourth_row = "    ".join(num.center(len(num_strs[i])) for i, num in enumerate(random_strs))

    print(first_row)
    print(second_row)
    print(third_row)
    print(fourth_row)


def find_ith_node(head: Node, i: int):
    start = head
    c = 0
    while c < i:
        start = start.next
        c += 1

    return start


def create_node_list(list: List[List[int]]):
    if not list:
        return

    head = Node(list[0][0])
    start = head
    n = len(list)

    for i in range(1, n):
        start.next = Node(list[i][0])
        start = start.next

    start = head
    for i in range(n):
        if list[i][1] is not None:
            node = find_ith_node(head, list[i][1])
            start.random = node
        start = start.next

    return head


# # Test Case 1
# start = create_node_list([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
# print_node_list(start)
# Solution().testCopyRandomList(start, start)

# # Test Case 2
start = create_node_list([[-1, 0]])
print_node_list(start)
Solution().testCopyRandomList(start, start)

# # Test Case 3
# start = create_node_list([[1, 2], [2, 2], [3, None], [4, None]])
# print_node_list(start)
# Solution().testCopyRandomList(start, start)

# Test Case 4
# start = create_node_list([[6, 5], [5, None], [3, 2], [-1, 20], [1, 21], [6, 21], [5, 9], [9, 9], [0, 5], [-7, 4], [-4, 22], [-6, None],
#                          [-1, None], [-6, None], [-8, 18], [-10, None], [-3, 2], [2, 16], [-8, 4], [0, None], [-1, None], [6, 13], [-7, 2]])
# print_node_list(start)
# Solution().testCopyRandomList(start, start)
