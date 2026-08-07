class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        l, r = height[0], height[len(height) - 1]
        ans = 0
        while i < j:
            if height[i] < height[j]:
                i += 1
                if height[i] > l:
                    l = height[i]
                else:
                    ans += (l - height[i])
            else:
                j -= 1
                if height[j] > r:
                    r = height[j]
                else:
                    ans += (r-height[j])
        return ans

