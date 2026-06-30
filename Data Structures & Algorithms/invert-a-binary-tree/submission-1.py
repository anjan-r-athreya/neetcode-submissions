# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        finalroot = root

        def reverse(root):
            if root == None:
                return None
            
            if root.left or root.right:
                temp = root.left

                if root.right:
                    root.left = root.right
                else:
                    root.left = None
                
                if temp:
                    root.right = temp
                else:
                    root.right = None
            
            reverse(root.left)
            reverse(root.right)
        
        reverse(root)
        return finalroot