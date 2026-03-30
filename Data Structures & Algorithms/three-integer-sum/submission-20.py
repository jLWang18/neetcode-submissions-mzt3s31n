class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            start = i + 1
            end = len(nums) - 1
            while start < end:
                res = first + nums[start] + nums[end]
                if res < 0:
                    start += 1
                elif res > 0:
                    end -= 1
                else:
                    out.append([first, nums[start], nums[end]])
                    end -= 1
                    start += 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
        return out