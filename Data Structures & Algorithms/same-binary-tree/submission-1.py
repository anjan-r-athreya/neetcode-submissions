# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        same = True
        
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]):
            nonlocal same

            if not p and not q:
                return
            elif not p or not q:
                same = False
                return 
            
            if p.val == q.val:
                dfs(p.left, q.left)
                dfs(p.right, q.right)
            elif p.val != q.val:
                same = False
                return
        
        dfs(p, q)
        return same