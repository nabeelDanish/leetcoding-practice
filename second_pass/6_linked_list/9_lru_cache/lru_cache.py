from typing import List


class LRUCache:
    class ListNode:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}
        self.pointer = 0
        self.head = None
        self.next = None

    def get(self, key: int) -> int:
        node = self.dict.get(key)
        if node is None:
            return -1

        # If the node is not the last node, move it to the end
        if node.next is not None:
            # If the node is the head, update the head
            if node.prev is not None:
                node.prev.next = node.next
            else:
                self.head = node.next

            # If the node is not the last node, update the next node
            node.next.prev = node.prev
            self.next.next = node

            # Update the node
            node.prev = self.next
            node.next = None

            # Update the next node
            self.next = node

        return node.value

    def put(self, key: int, value: int) -> None:
        # If the key already exists, update the value and move the node to the end
        if self.dict.get(key) is not None:
            self.dict[key].value = value
            self.get(key)
            return
        
        # Inserting a new node in the double linked list if it doesn't already exist
        if self.head is None:
            self.head = self.ListNode(key, value)
            self.dict[key] = self.head
        elif self.next is None:
            self.next = self.ListNode(key, value)
            self.head.next = self.next
            self.next.prev = self.head
            self.dict[key] = self.next
        else:
            self.next.next = self.ListNode(key, value)
            self.next.next.prev = self.next
            self.next = self.next.next
            self.dict[key] = self.next

        # If the capacity is reached, remove the least recently used element
        # which is the head of the linked list
        self.pointer += 1
        if self.pointer > self.capacity:
            self.dict.pop(self.head.key)
            self.head = self.head.next
            self.head.prev = None
            self.pointer -= 1


class TestLRUCache:
    def test(self, commands: List[str], inputs: List, expected: List):
        lru_cache = None
        for i, command in enumerate(commands):
            if command == "LRUCache":
                lru_cache = LRUCache(inputs[i][0])
            elif command == "get":
                actual = lru_cache.get(inputs[i][0])
                assert actual == expected[i], f"Test Case Failed! actual: {actual} expected: {expected[i]}"
            else:
                lru_cache.put(inputs[i][0], inputs[i][1])
        print("Test Case Passed!")


TestLRUCache().test(
    ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
    [None, None, None, 1, None, -1, None, -1, 3, 4]
)

TestLRUCache().test(
    ["LRUCache", "put", "put", "get", "put", "put", "get"],
    [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]],
    [None, None, None, 2, None, None, -1]
)
