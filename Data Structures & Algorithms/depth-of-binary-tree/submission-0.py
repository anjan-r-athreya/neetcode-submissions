# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxdepth = 1

        def dive(node, count = 0):
            nonlocal maxdepth

            if node == None:
                maxdepth = 0
                return

            if not node.left and not node.right:
                if count > maxdepth:
                    maxdepth = count
            elif node.left and node.right:
                dive(node.left, count + 1)
                dive(node.right, count + 1)
            elif not node.right:
                dive(node.left, count + 1)
            elif not node.left:
                dive(node.right, count + 1)
        
        dive(root, 1)
        return maxdepth
                