from typing import List


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
        previous_node: TrieNode = self.starts.get(word[0], None)
        if previous_node is None:
            previous_node = TrieNode(word[0])
            self.starts[word[0]] = previous_node

        for i in range(1, n):
            if word[i] not in previous_node.children:
                previous_node.children[word[i]] = TrieNode(word[i])
            previous_node = previous_node.children[word[i]]

        previous_node.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # we will first create a trie from the list of words, and then we will iterate through the board and check if each letter is in the trie,
        # if it is, we will continue checking the adjacent letters until we find a word in the trie or we reach the end of the board
        trie = Trie()
        for word in words:
            trie.insert(word)

        found_words = []
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.starts:
                    self._findWordsHelper(board, trie.starts[board[i][j]], i, j, visited, board[i][j], found_words)

        # remove duplicates from found_words
        return list(set(found_words))

    def _findWordsHelper(self, board: List[List[str]], trie_node: TrieNode, i: int, j: int, visited: List[List[bool]], current_word: str, found_words: List[str]):
        if trie_node.is_word:
            found_words.append(current_word)

        visited[i][j] = True

        # we will check the adjacent letters in the board, and if they are in the trie, we will continue checking them
        for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and not visited[x][y] and board[x][y] in trie_node.children:
                self._findWordsHelper(board, trie_node.children[board[x][y]], x, y, visited, current_word + board[x][y], found_words)

        visited[i][j] = False

    def testFindWords(self, board: List[List[str]], words: List[str], expected: List[str]):
        actual = self.findWords(board, words)
        if set(actual) != set(expected):
            print(f"Test Case Failed! -- board: {board}, words: {words}\nactual: {actual}, expected: {expected}")
        else:
            print(f"Test Case Passed!")


Solution().testFindWords(
    board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
    words=["oath", "pea", "eat", "rain"],
    expected=["eat", "oath"]
)
Solution().testFindWords(
    board=[["a", "b"], ["c", "d"]],
    words=["abcb"],
    expected=[]
)
Solution().testFindWords(
    board=[["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]],
    words=["oa", "oaa"],
    expected=["oa", "oaa"]
)
