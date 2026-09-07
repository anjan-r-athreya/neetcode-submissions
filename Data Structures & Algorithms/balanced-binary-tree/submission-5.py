# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(node: Optional[TreeNode]):
            nonlocal balanced

            if not node:
                return 0
            
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            balanced = balanced and abs(left - right) <= 1

            return max(left, right)

        dfs(root)

        return balanced