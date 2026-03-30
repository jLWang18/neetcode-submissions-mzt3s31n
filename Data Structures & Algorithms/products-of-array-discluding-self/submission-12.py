class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = [1 for _ in range(len(nums))]
        
        lp = 1
        for i in range(len(out)):
            out[i] *= lp
            lp *= nums[i]

        rp = 1
        for i in range(len(out) - 1, -1, -1):
            out[i] *= rp
            rp *= nums[i]
        return out