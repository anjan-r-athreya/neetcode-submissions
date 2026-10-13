# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        currsum = 0

        def dfs(node: Optional[TreeNode], currsum):
            if not node:
                return False

            currsum += node.val

            if node.right == None and node.left == None:
                return currsum == targetSum
            
            left = dfs(node.left, currsum)
            right = dfs(node.right, currsum)

            return left or right
        
        return dfs(root, 0)