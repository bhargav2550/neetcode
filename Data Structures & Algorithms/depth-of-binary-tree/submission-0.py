# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def f(root):
            if not root:
                return -1e9
            if root.left == None and root.right == None:
                return 1
            return 1 + max(f(root.left),f(root.right))
        ans = f(root)
        if ans == -1e9: return 0
        return ans