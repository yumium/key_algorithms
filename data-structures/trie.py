class Trie:
    def __init__(self,words=[]):
        self.root = TrieNode("",{},True)
        for w in words:
            self.add(w)

    def print(self):
        self.root.print(0)

    def add(self,w):
        '''
        Inserts the word *w* into the Trie
        :type w: str
        :rtype: None
        '''
        node = self.root

        i = 0
        # Invariant: node is at last character of w[0..i)
        while i < len(w):
            if w[i] not in node.child:
                node.child[w[i]] = TrieNode(w[i],{},False)
            node = node.child[w[i]]
            i += 1
        node.isWord = True
        
    def contain(self,w):
        '''
        Return if word *w* is in the Trie
        :type w: str
        :rtype: bool
        '''
        node = self._findPrefix(w)
        return node and node.isWord


    def startWith(self, prefix):
        '''
        Return if *prefix* is a prefix in the Trie
        :type prefix: str
        :rtype: bool
        '''
        return bool(self._findPrefix(prefix))
        

    def _findPrefix(self,prefix):
        '''
        Helper that finds *prefix* in the Trie
        Returns the last node of the prefix if found
        Returns None if not
        :type prefix: str
        :rtype: TrieNode
        '''
        node = self.root

        for c in prefix:
            if c not in node.child:
                return None
            node = node.child[c]
        return node

class TrieNode:
    def __init__(self,data,child,isWord):
        self.data = data
        self.isWord = isWord
        self.child = child  # map char -> TrieNode

    def print(self,d):
        out = ".." * d
        if self.isWord:
            out += color.RED + self.data + color.END
        else:
            out += self.data
        print(out)
        for c in sorted(self.child.keys()):
            self.child[c].print(d+1)