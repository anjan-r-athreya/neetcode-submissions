# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # return leaf
        # intersection: compute order of the three values:
        #   left, right, parent
        # track in a updated increasing list representing the increasing order of the elements
        # once the list reaches length k, return list[-1]
        count = 0
        result = 0

        def buildInc(node: Optional[TreeNode]):
            nonlocal count
            nonlocal result

            if not node:
                return
            
            if node.left: buildInc(node.left)

            # do something with root
            count += 1
            if count == k:
                result = node.val
                return 

            if node.right: buildInc(node.right)

        buildInc(root)
        return result
