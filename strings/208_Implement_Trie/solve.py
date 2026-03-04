class Trie:

    def __init__(self):
        self.store = {}

    def insert(self, word: str) -> None:
            self.store[word] = word

    def search(self, word: str) -> bool:
        if self.store.get(word,None):
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
            for word in self.store:
                if prefix in word[:len(prefix)]:
                    return True
            return False

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)