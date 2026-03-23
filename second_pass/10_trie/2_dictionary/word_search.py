class TrieNode:
    letter: str
    is_word: bool
    children = None

    def __init__(self, letter: str, is_word: bool = False):
        self.letter = letter
        self.is_word = is_word
        self.children = {}


class WordDictionary:

    def __init__(self):
        self.starts = {}

    def addWord(self, word: str) -> None:
        n = len(word)
        previous_node: TrieNode = self.starts.get(word[0], None)
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

        if word[0] == ".":
            for key in self.starts:
                if self._search_helper(word, 0, self.starts[key]):
                    return True
            return False
        else:
            previous_node: TrieNode = self.starts.get(word[0], None)
            if previous_node is None:
                return False
            return self._search_helper(word, 0, previous_node)

    def _search_helper(self, word: str, index: int, node: TrieNode) -> bool:
        if index == len(word) - 1:
            return node.is_word

        if word[index + 1] == ".":
            for key in node.children:
                if self._search_helper(word, index + 1, node.children[key]):
                    return True
            return False
        else:
            if word[index + 1] not in node.children:
                return False
            return self._search_helper(word, index + 1, node.children[word[index + 1]])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
instructions = ["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"]
inputs = [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]]
outputs = [None, None, None, None, False, True, True, True]

obj = None
failed = False
for i, instruction in enumerate(instructions):
    if instruction == "WordDictionary":
        obj = WordDictionary()
    elif instruction == "addWord":
        obj.addWord(inputs[i][0])
    elif instruction == "search":
        if obj.search(inputs[i][0]) != outputs[i]:
            print(f"Failed on instruction {i} with input {inputs[i]} and output {outputs[i]}")
            failed = True
            break

if not failed:
    print("Test Case Passed!")
