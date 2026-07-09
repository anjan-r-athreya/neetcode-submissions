# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        finalroot = root

        def reverse(node: Optional[TreeNode]):
            if node == None:
                return

            if node.left != None and node.right != None:
                temp = node.right
                node.right = node.left
                node.left = temp
                reverse(node.left)
                reverse(node.right)
            elif node.right == None:
                node.right = node.left
                node.left = None
                reverse(node.right)
            elif node.left == None:
                node.left = node.right
                node.right = None
                reverse(node.left)

        reverse(root)
        return finalroot