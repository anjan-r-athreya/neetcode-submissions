# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        valid = True
        
        def isValid(root: Optional[TreeNode], mi, ma):
            nonlocal valid

            if not root: return

            if root.val >= mi or root.val <= ma:
                valid = False
            else:
                valid = valid and True
            
            isValid(root.left, root.val, ma)
            isValid(root.right, mi, root.val)
        
        isValid(root, float('inf'), float('-inf'))
        return valid
