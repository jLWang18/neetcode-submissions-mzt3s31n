class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]

        my_dict = {}
        for num in nums:
            my_dict[num] = 1 + my_dict.get(num, 0)
        
        
        for num, freq in my_dict.items():
            bucket[freq].append(num)
        
        out = []
        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i] != None:
                for num in bucket[i]:
                    out.append(num)
                if len(out) == k:
                    return out
