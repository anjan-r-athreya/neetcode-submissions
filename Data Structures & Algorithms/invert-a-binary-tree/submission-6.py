# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        final = root

        def invert(node: Optional[TreeNode]):
            if not node or (not node.left and not node.right):
                return
            elif node.left and node.right == None:
                # right just takes node left and we delete left
                node.right = node.left
                node.left = None
            elif node.right and node.left == None:
                node.left = node.right
                node.right = None
            else:
                temp = node.left
                node.left = node.right
                node.right = temp

                invert(node.left)
                invert(node.right)
        
        invert(root)

        return final