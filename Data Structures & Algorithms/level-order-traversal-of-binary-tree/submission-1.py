# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        queue = deque([root])
        visited = {root}
        layers = []

        while queue:
            size = len(queue)
            curr_layer = []

            for i in range(size):
                curr = queue.popleft()
                curr_layer.append(curr.val)

                for neighbor in [curr.left, curr.right]:
                    if neighbor and neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

            layers.append(curr_layer)
        
        return layers
        

"""
bfs pseudocode:

n = num nodes
queue = deque([start])
visited = set(start)
layers = []

while queue:
    size = len(queue)
    curr_layer = []

    for i in range(size):
        curr = queue.popleft()
        curr_layer.append(curr)
        visited.add(curr)

        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    layers.append(curr_layer)

"""