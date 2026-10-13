# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        currsum = 0

        def dfs(node: Optional[TreeNode], targetsum):
            if not node:
                return False

            targetsum -= node.val

            if node.right == None and node.left == None:
                return targetsum == 0
            
            left = dfs(node.left, targetsum)
            right = dfs(node.right, targetsum)

            return left or right
        
        return dfs(root, targetSum)