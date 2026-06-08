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
    bool isBalanced(TreeNode* root) {
        return dfs(root).first;
    }

private:
    pair<bool, int> dfs(TreeNode* node) {
        if(node == nullptr)
            return {true, 0};
        pair<bool, int> left = dfs(node->left);
        pair<bool, int> right = dfs(node->right);

        int height = max(left.second, right.second) + 1;
        bool balanced = left.first and right.first and (abs(left.second - right.second) <= 1);

        return {balanced, height};
    }
    
};
