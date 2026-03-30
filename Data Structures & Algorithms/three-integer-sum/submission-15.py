class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        out = []
        for i in range(len(nums)):
            print(f"index = {i}")
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                res = first + nums[left] + nums[right]
                print(f"{first} + {nums[left]} + {nums[right]} = {res}")
                if res > 0:
                    right -= 1
                elif res < 0:
                    left += 1
                elif res == 0:
                    print("yeay")
                    out.append([first, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return out