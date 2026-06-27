# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lBound, rBound):
            if not root:
                return True
            
            res = root.val > lBound and root.val < rBound
            if root.left:
                res = res and helper(root.left, lBound, root.val)
            if root.right:
                res = res and helper(root.right, root.val, rBound)
            
            return res
        
        return helper(root, -1001, 1001)