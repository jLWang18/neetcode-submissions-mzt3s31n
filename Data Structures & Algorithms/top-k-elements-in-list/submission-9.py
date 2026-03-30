class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        print(bucket)
        
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        print(count)
        for num, freq in count.items():
            print(num)
            print(freq)
            bucket[freq].append(num)
        
        out = []
        for i in range(len(bucket) - 1, 0, -1):
            if bucket[i] != None:
                for num in bucket[i]:
                    out.append(num)
                
                if len(out) == k:
                    return out
