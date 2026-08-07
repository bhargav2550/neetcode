# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        st = []
        ans = []
        while curr or st:
            if curr:
                ans.append(curr.val)
                st.append(curr)
                curr = curr.right
            else:
                curr = st.pop()
                curr = curr.left
        return ans[::-1]