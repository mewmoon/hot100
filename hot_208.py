# 208 实现Tier(前缀树)


class Trie(object):
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def searchPrefix(self, prefix):
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.searchPrefix(prefix)
        return node is not None


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
trie.insert("app")
print(trie.search("app"))
