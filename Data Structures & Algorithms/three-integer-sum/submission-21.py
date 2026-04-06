class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            f = i + 1
            l = len(nums) - 1
            while f < l:
                res = first + nums[f] + nums[l]
                if res < 0:
                    f += 1
                elif res > 0:
                    l -= 1
                else:
                    out.append([first, nums[f], nums[l]])
                    l -= 1
                    f += 1
                    while f < l and nums[f] == nums[f-1]:
                        f += 1
        return out