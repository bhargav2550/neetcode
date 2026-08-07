class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = defaultdict(int)
        n = len(nums)
        ele1, ele2 = 0,0
        cnt1, cnt2 = 0,0

        for i in nums:
            if cnt1 == 0:
                ele1 = i
                cnt1 += 1
            elif cnt2 == 0 and i != ele1:
                ele2 = i
                cnt2 += 1
            elif ele1 == i:
                cnt1 += 1
            elif ele2 == i:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        ans = []
        if nums.count(ele1) > n // 3:
            ans.append(ele1)
        if nums.count(ele2) > n // 3:
            ans.append(ele2)
        return ans