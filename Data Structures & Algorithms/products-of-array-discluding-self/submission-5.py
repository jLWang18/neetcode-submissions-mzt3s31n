class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        # map index with num
        my_dict = {}
        for i in range(len(nums)):
            my_dict[i] = nums[i]
        
        for i in range(len(nums)):
            prod = 1
            for index, num in my_dict.items():
                if index != i:
                    prod *= num
            out.append(prod)
        return out