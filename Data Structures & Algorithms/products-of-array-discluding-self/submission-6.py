class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [ 1 for _ in range(len(nums))]
        # from left to right
        left_pointer_product = 1
        for i in range(len(nums)):
            out[i] = out[i] * left_pointer_product
            left_pointer_product = left_pointer_product * nums[i]
        
        # from right to left
        right_pointer_product = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] = out[i] * right_pointer_product
            right_pointer_product = right_pointer_product * nums[i]
        return out 