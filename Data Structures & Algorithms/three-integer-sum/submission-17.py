class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                res = first + nums[left] + nums[right]
                if res > 0:
                    right -= 1
                elif res < 0:
                    left += 1
                else:
                    out.append([first, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    right -= 1
        return out