class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dict = {}
        
        for i in range(len(numbers)):
            comp = target - numbers[i]
            if comp in num_dict:
                return [num_dict[comp], i+1]
            num_dict[numbers[i]] = i + 1
            print(num_dict)
        return []
    