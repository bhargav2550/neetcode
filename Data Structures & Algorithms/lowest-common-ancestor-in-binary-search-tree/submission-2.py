# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        from collections import deque
        parent = {root: None}
        queue = deque([root])

        while p not in parent or q not in parent:

            node = queue.popleft()

            if node.left:
                parent[node.left] = node
                queue.append(node.left)
            
            if node.right:
                parent[node.right] = node
                queue.append(node.right)
        
        # add all ancestors of p
        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]
        
        # check which is the LCA with p ancestors
        while q not in ancestors:
            q = parent[q]
        return q
            