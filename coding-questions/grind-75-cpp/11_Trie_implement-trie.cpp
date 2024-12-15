#include <map>
#include <string>
#include <optional>
#include <iostream>

using namespace std;

class Node {
public:
    bool is_word = false;
    map<char, Node> child;
};

class Trie {
public:
    /* Inserts the string `word` into the Trie, assuming all words are nonempty */
    void insert(string word) {
        Node* node = &head;

        for (auto c: word) {
            if (node->child.find(c) == node->child.end())
                node->child[c] = Node{}; // is this correct?
            node = &(node->child[c]);
        }

        node->is_word = true;
    }
    
    /* Returns whether `word` is in the Trie */
    bool search(string word) {
        auto node = find(word);
        return node != nullptr && node->is_word;
    }
    
    /* Returns whether `prefix` is a prefix of a word in the Trie */
    bool startsWith(string prefix) {
        return find(prefix) != nullptr;
    }

    Node head;
private:
    // Explore returning nullptr, can I still use std::optional but avoid copying?
    Node* find(string word) {
        Node* node = &head;
        
        for (auto c: word) {
            if (node->child.find(c) == node->child.end()) {
                cout << c << " not found" << endl;
                return nullptr;

            }
            node = &(node->child[c]);
        }

        return node;
    }
};

int main() {
    Trie obj;
    auto& head = obj.head;
    obj.insert("banana");
    cout << obj.search("banana") << endl;
    cout << obj.startsWith("bana") << endl;
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */