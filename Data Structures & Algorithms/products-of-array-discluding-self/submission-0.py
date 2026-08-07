class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        suf = [1]*n
        ans = []
        for i in range(1,n):
            pre[i] = pre[i-1] * nums[i-1]
        for i in range(n-2,-1,-1):
            suf[i] = suf[i+1] * nums[i+1]
        
        for i,j in zip(pre,suf):
            ans.append(i*j)
        return ans
            