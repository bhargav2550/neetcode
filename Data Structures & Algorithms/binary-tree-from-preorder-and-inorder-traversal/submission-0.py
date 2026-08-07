# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inordermap = {num:ind for ind,num in enumerate(inorder)}

        def helper(l,r):
            if l > r:
                return 
            root = TreeNode(preorder.pop(0))
            idx = inordermap[root.val]
            root.left = helper(l, idx-1)
            root.right = helper(idx+1, r)
            return root
        return helper(0,len(preorder)-1)