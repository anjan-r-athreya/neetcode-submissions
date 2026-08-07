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
            elif root.left and root.right:
                temp = root.left
                root.left = root.right
                root.right = temp
                reverse(root.left)
                reverse(root.right)
            elif root.left:
                root.right = root.left
                reverse(root.right)
            elif root.right:
                root.left = root.right
                reverse(root.left)
        
        reverse(root)
        return finalroot