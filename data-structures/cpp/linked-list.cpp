struct Node {
    int val;
    Node *next;
    Node(int val, Node *next = nullptr) : val(val), next(next) {}
};