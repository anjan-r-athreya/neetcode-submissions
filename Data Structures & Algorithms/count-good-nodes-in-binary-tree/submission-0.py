# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # all we need to compare against is the maximum value we see on a path so far
        # question: if curr_max == node.val, is that a good node?

        if not root:
            return 0

        count = 0 # the root is always a good node
        curr_max = root.val

        def dfs(node: TreeNode, curr_max):
            nonlocal count

            if not node:
                return

            if node.val >= curr_max:
                curr_max = node.val
                count += 1
            
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

        dfs(root, curr_max)
        return count