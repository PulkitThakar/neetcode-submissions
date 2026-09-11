# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        s = []

        curr = root
        while curr or s:
            while curr:
                s.append(curr)
                curr = curr.left
            
            curr = s.pop()
            res.append(curr.val)
            curr = curr.right
        return res
