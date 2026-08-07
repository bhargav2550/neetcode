# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = []
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = None
        curr = root
        st = []
        while curr or st:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            if pre and pre.val >= curr.val:
                return False
            pre = curr
            curr = curr.right
        return True