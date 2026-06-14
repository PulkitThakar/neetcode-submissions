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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res;
        dfs(root, 0, res);
        return res;
    }
private:
    void dfs(TreeNode* node, int track, vector<int>& res) {
        if(node == nullptr)
            return;
        
        if(track == res.size())
            res.push_back(node->val);
        
        dfs(node->right, track + 1, res);
        dfs(node->left, track + 1, res);

        return;
    }
};
