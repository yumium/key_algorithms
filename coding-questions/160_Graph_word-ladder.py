class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        Given:
            beginWord: The word to begin with, doesn't need to be in `wordList`
            endWord: The word to end with, in `wordList`
            wordList: A list of words
                1 <= len(wordList) <= 5000
                All words in `wordList` are unique

                `beginWord` != `endWord`
                1 <= len(beginWord) = len(endWord) = len(wordList[i]) <= 10
                All words are made up of lowercase English letters

        Return:
            The # of transformations to get from `beginWord` to `endWord` using words in `wordList`.
            Return 0 if no path is possible
        
        Ideas:
        - Remind me of AI Search

        - BFS, DFS, Depth limited search, A* search

        - BFS: nodes = `wordList` + `beginWord`, edges = 1 letter apart
        - TIME: O(NK)
        - SPACE: O(N)
        '''
        wordList = set(wordList)
        queue = collections.deque([[beginWord, 1]])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + c + word[i+1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        queue.append([next_word, length + 1])
        return 0

        # A* algorithm
