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
                print(prod)
                print(num)
                if index != i:
                    prod *= num
                    print("product res = " + str(prod) + "/n")
                    
            out.append(prod)
        return out