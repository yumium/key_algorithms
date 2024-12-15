/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    /*
        Given:
            root: Pointer to the root of a BT
                1 <= N <= 1E4
                deltype(Node.val) = int32_t

        Return:
            Whether the BT is valid or not

        Ideas:
        - In-order traversal
            - TIME: O(N)
            - SPACE: O(N)
        - Recursion, returning bounds
    */
    bool isValidBST(TreeNode* root) {
        stack<TreeNode*> stack;
        bool is_first = true;
        int32_t prev_val;
        
        while (root != nullptr || !stack.empty()) {
            if (root != nullptr) 
            {
                stack.push(root);
                root = root->left;
            }
            else 
            {
                root = stack.top();
                stack.pop();
                if (is_first) 
                    is_first = false;
                else if (prev_val >= root->val) 
                    return false;
                prev_val = root->val;
                root = root->right;
            }
        }

        return true;
    }
};