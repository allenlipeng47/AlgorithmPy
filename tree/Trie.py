class TrieNode(object):

    def __init__(self):
        self.nodes = {}
        self.word = None

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.nodes:
                curr.nodes[ch] = TrieNode()
            curr = curr.nodes[ch]
        curr.word = word

    def search(self, word):
        curr = self.root
        for ch in word:
            if ch not in curr.nodes:
                return False
            curr = curr.nodes[ch]
        if curr.word is not None:
            return True
        return False

    def startsWith(self, prefix):
        curr = self.root
        for ch in prefix:
            if ch not in curr.nodes:
                return False
            curr = curr.nodes[ch]
        return True

trie = Trie()
trie.insert('aaaa')
trie.insert('abc')
print (trie.startsWith('aa'))
print (trie.search('abc'))
print (trie.search('ab'))
print (trie.search('abcd'))