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

            if not node: return 0

            left, right = dfs(node.left), dfs(node.right)

            diff = abs(left - right) <= 1

            if diff == False:
                balanced = diff
            return max(left, right) + 1
        
        dfs(root)
        return balanced