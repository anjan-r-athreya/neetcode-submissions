# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        output = []

        def level(node, levelcurr):
            nonlocal output

            if not node:
                return
            
            if len(output) == levelcurr:
                output.append([])
            
            output[levelcurr].append(node.val)

            level(node.left, levelcurr + 1)
            level(node.right, levelcurr + 1)

        level(root, 0)
        
        return output