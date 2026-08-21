# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subTree = False

        def findRoot(node: Optional[TreeNode]):
            nonlocal subTree

            if not node: return

            if node.val == subRoot.val:
                subTree = isSame(node, subRoot)

            if subTree == True: return
            
            findRoot(node.left)
            findRoot(node.right)

        def isSame(p: Optional[TreeNode], q: Optional[TreeNode]):
            if not p and not q: return True

            if not p or not q: return False

            if p.val != q.val: return False

            return isSame(p.left, q.left) and isSame(p.right, q.right)

        findRoot(root)
        return subTree
