class TrieNode:
    def __init__(self):
        self.children = {}
        self.endWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    # Hàm để thêm một từ vào Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endWord = True
    
    # Hàm in cây Trie
    def printTrie(self):
        self._printTrie(self.root, "")
    
    def _printTrie(self, node, current):
        if node.endWord == True:
            print(current)
        
        for char, childNode in node.children.items():
            self._printTrie(childNode, current + char)

# Dữ liệu đầu vào
products = ["cat", "banana", "obama", "batman", "car", "cow", "alibaba", "cart", "catch", "on", "at"]

# Tạo cây Trie và thêm từng từ vào
trie = Trie()
for item in products:
    trie.insert(item)

# In cây Trie
trie.printTrie()
