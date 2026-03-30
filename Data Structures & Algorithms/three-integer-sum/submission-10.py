class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i, val in enumerate(nums):
            if i > 0 and nums[i-1] == val:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = val + nums[left] + nums[right]
                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    out.append([val, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
        return out 