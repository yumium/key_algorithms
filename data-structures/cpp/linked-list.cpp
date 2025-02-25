#include <sstream>
#include <iostream>
#include <memory>

struct Node {
    int val;
    std::unique_ptr<Node> next;
    Node(int val) : val(val), next(nullptr) {}
    Node(int val, std::unique_ptr<Node> next) : val(val), next(std::move(next)) {}
};

class LinkedList {
public:
    bool insert(int val, size_t pos) {
        std::unique_ptr<Node>* cur = &_head;
        while (pos > 0 && (*cur)->next) {
            cur = &((*cur)->next);
            pos--;
        }

        if (pos > 0) return false;
        (*cur)->next = std::make_unique<Node>(val, std::move((*cur)->next));
        
        return true;
    }

    bool remove(size_t pos) {
        std::unique_ptr<Node>* cur = &_head;
        while (pos > 0 && (*cur)->next) {
            cur = &((*cur)->next);
            pos--;
        }
        
        if (pos > 0 || !(*cur)->next) return false;

        (*cur)->next = std::move((*cur)->next->next);
        return true;
    }

    std::string to_string() {
        bool first = true;
        std::ostringstream ret;
        Node* cur = _head->next.get();
        while (cur) {
            if (first) {
                ret << cur->val;
                first = false;
            }
            else ret << ", " << cur->val;

            cur = cur->next.get();
        }

        return ret.str();
    }

private:
    std::unique_ptr<Node> _head = std::make_unique<Node>(0);  // dummy node
};

int main() {
    auto ll = LinkedList();
    ll.insert(1, 0);
    ll.insert(2, 1);
    ll.insert(4, 2);
    std::cout << ll.to_string() << std::endl;

    // after removal
    std::cout << ll.remove(1) << std::endl;
    std::cout << ll.to_string() << std::endl;
}