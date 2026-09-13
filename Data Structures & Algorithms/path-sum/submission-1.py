# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, target):
            if not root:
                return False

            
            temp = target - root.val
            if not (root.left or root.right):
                return temp == 0

            return dfs(root.left, temp) or dfs(root.right, temp)
        
        return dfs(root, targetSum)