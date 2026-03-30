class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in my_dict:
                return [my_dict[comp], i]
            my_dict[nums[i]] = i
        return []
