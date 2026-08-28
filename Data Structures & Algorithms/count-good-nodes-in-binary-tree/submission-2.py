# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def f(root, ans):
            nonlocal result
            if not root:
                return 0
            if root.val >= ans:
                if result == -1e9:
                    result = 1
                else:
                    result += 1
            left = f(root.left, max(ans,root.val))
            right = f(root.right, max(ans, root.val))

        f(root, -1e9)
        return result
            
