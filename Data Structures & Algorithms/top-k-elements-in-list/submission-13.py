class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, freq in count.items():
            bucket[freq].append(num)
        print(bucket)
        out = []
        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i] != None:
                if len(out) == k:
                    return out
                for num in bucket[i]:
                    out.append(num)
        return out               
