# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # what do we have to keep track of: 
        # where p is
        # where q is

        def traverse(node: TreeNode, p: TreeNode, q: TreeNode):
            if (p.val <= node.val and q.val >= node.val) or (p.val >= node.val and q.val <= node.val):
                return node
            elif p.val < node.val and q.val < node.val:
                return traverse(node.left, p, q)
            elif p.val > node.val and q.val > node.val:
                return traverse(node.right, p, q)
        
        return traverse(root, p, q)
        
        # we need to return the value of the node for the recursion
