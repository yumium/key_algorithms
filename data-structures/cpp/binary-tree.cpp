#include <iostream>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x, TreeNode *left = nullptr, TreeNode *right = nullptr) : val(x), left(left), right(right) {}
};

int main() {
    auto tn = TreeNode(42);
    std::cout << tn.val << std::endl;
}