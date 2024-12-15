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
            root: TreeNode
                0 <= N <= 2000
                -1000 <= Node.val <= 1000
        
        Return:
            Level order traversal of nodes, vector of vector (one for each level, left to right)

        Time: O(N)
        Space: O(N)
    */
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> res {};
        if (!root)
            return res;
        
        vector<int> row {root->val};
        queue<pair<TreeNode*, int>> q;
        if (root->left)
            q.push({root->left, 1});
        if (root->right)
            q.push({root->right, 1});
        int prev_depth = 0;

        while (!q.empty()) {
            auto elem = q.front();
            q.pop();
            const TreeNode* node = elem.first;
            const int depth = elem.second;
            if (depth > prev_depth) {
                res.push_back(row);
                row = {node->val};
                prev_depth += 1;
            } else {
                row.push_back(node->val);
            }

            if (node->left)
                q.push({node->left, depth+1});
            if (node->right)
                q.push({node->right, depth+1});
        }

        res.push_back(row);
        return res;
    }
};