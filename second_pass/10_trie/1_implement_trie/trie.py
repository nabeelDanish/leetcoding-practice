class TrieNode:
    letter: str
    is_word: bool
    children = None

    def __init__(self, letter: str, is_word: bool = False):
        self.letter = letter
        self.is_word = is_word
        self.children = {}


class Trie:

    def __init__(self):
        self.starts = {}

    def insert(self, word: str) -> None:
        n = len(word)
        previous_node = self.starts.get(word[0], None)
        if previous_node is None:
            previous_node = TrieNode(word[0])
            self.starts[word[0]] = previous_node

        for i in range(1, n):
            if word[i] not in previous_node.children:
                previous_node.children[word[i]] = TrieNode(word[i])
            previous_node = previous_node.children[word[i]]

        previous_node.is_word = True

    def search(self, word: str) -> bool:
        n = len(word)
        previous_node = self.starts.get(word[0], None)
        if previous_node is None:
            return False

        for i in range(1, n):
            if word[i] not in previous_node.children:
                return False
            previous_node = previous_node.children[word[i]]

        return (previous_node and previous_node.is_word)

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        previous_node = self.starts.get(prefix[0], None)
        if previous_node is None:
            return False

        for i in range(1, n):
            if prefix[i] not in previous_node.children:
                return False
            previous_node = previous_node.children[prefix[i]]

        return (previous_node is not None)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
instructions = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
inputs = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
outputs = [None, None, True, False, True, None, True]

obj = None
failed = False
for i, instruction in enumerate(instructions):
    if instruction == "Trie":
        obj = Trie()
    elif instruction == "insert":
        obj.insert(inputs[i][0])
    elif instruction == "search":
        actual = obj.search(inputs[i][0])
        if actual != outputs[i]:
            print(f"Test Case Failed! -- instruction: {instruction} -- input: {inputs[i][0]}\nactual: {actual}, expected: {outputs[i]}")
            failed = True
            break
    elif instruction == "startsWith":
        actual = obj.startsWith(inputs[i][0])
        if actual != outputs[i]:
            print(f"Test Case Failed! -- instruction: {instruction} -- input: {inputs[i][0]}\nactual: {actual}, expected: {outputs[i]}")
            failed = True
            break

if not failed:
    print(f"Test Case Passed!")
