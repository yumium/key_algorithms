# Source: https://leetcode.com/problems/top-k-frequent-words/

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        '''
        Given:
            words: An array of strings
                1 <= len(words) <= 500
                1 <= len(words[i]) <= 10
            k: Top # most frequence strings
                1 <= k <= # of unique words in `words`
        Return:
            k most frequence words, sort words with same frequency in lexicographic order
        
        - Tally the words {word -> count}
        - Reverse the mapping {count -> [words]}
        - Sort list of [(-count, word)] in ascending order, take first k
        
        TIME: O(N log N)
        SPACE: O(N)
        '''
        tally = {}
        for w in words:
            if w not in tally:
                tally[w] = 1
            else:
                tally[w] += 1
    
        count = []  # A list of (-count, word)
        for w in tally:
            count.append((-tally[w], w))
        
        count.sort()
        return [tup[1] for tup in count[:k]]

