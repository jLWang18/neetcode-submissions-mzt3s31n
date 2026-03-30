class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        
        my_dict = {}
        for num in nums:
            my_dict[num] = 1 + my_dict.get(num, 0)
        
        for num, freq in my_dict.items():
            bucket[freq].append(num)
        
        print(bucket)
        arr = []
        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i] != None:
                # loop the inside arr
                for num in bucket[i]:
                    arr.append(num)
                    print(arr)
                if len(arr) == k:
                    return arr
        return arr
