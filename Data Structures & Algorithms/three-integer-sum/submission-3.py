class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort() # make it easier to detect and skip duplicate

        for i, num in enumerate(nums):
            # if the num is the same as before it, skip it
            if i > 0 and num == nums[i-1]:
                continue

            # compute the rest of the nums, like you did it in Two Sum II
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    out.append([num, nums[left], nums[right]])
                    left += 1
                    # skip duplicate
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return out 
