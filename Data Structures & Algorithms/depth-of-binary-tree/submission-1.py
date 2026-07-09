# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dive(node):
            if node == None:
                return 0

            if not node.left and not node.right:
                return 1
            elif node.left and node.right:
                return max(dive(node.left), dive(node.right)) + 1
            elif not node.right:
                return dive(node.left) + 1
            elif not node.left:
                return dive(node.right) + 1

        return dive(root)
                