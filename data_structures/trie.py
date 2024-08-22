"""
The Trie data structure is a tree-like data structure used for storing a dynamic set of strings.
It is commonly used for efficient retrieval and storage of keys in a large dataset.
The structure supports operations such as insertion, search, and deletion of keys, making it a
valuable tool in fields like computer science and information retrieval.
"""

# Note This is for lower case words only
from collections import deque

class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # letters of the alphabet
        self.is_end = False

    def is_empty(self) -> bool:
        for child in self.children:
            if child:
                return False
        return False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word.lower():
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.is_end = True

    def has_word(self,  word: str) -> bool:
        cur = self.root
        for c in word.lower():
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return cur.is_end

    def starts_with(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix.lower():
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return True

    def delete(self, word: str) -> None:
        cur = self.root
        stack = []
        for c in word.lower():
            idx = ord(c) - ord('a')
            if cur.children[idx]:
                stack.append((idx, cur.children[idx]))
                cur = cur.children[idx]

        # We've reached the end of the word
        cur.is_end = False
        # clean up rollups if need
        while cur.is_empty() and not cur.is_end:
            child_index, prev = stack.pop() if stack else (None, None)
            if prev:
                prev.children[child_idx] = None

            cur = prev

    def print(self):
        cur = self.root
        queue = deque()
        current_level = 1
        for idx, child in enumerate(cur.children):
            if child:
                print(chr(ord('a')+idx), end=' ')
                queue.append((child, current_level))
        print()
        while queue:
            current_child, level = queue.popleft()
            if level > current_level:
                print()
                current_level = level
            for idx, child in enumerate(current_child.children):
                if child:
                    print(chr(ord('a')+idx), end=' ')
                    queue.append((child, current_level+1))
    # This should be a bfs to print the tree, to print the words we'd do a dfs

if __name__ == '__main__':
    keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "hero", "heroplane"]
    trie = Trie()
    for key in keys:
        trie.insert(key)

    trie.insert('the')
    assert trie.has_word('the')
    for key in keys:
        assert trie.has_word(key)

    assert trie.has_word('NOTHERE') == False
    assert trie.starts_with('by')
    assert trie.starts_with('theirs') == False

    trie.delete('by')
    assert trie.has_word('by') == False
    assert trie.has_word('bye')
    trie.delete('bye')
    assert trie.has_word('by') == False
    assert trie.has_word('bye') == False

    trie.print()
