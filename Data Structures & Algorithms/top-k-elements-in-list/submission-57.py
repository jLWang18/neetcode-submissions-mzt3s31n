class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for num, count in freq.items():
            bucket[count].append(num)
        
        out = []
        for i in range(len(bucket) -1, -1, -1):
            for num in bucket[i]:
                out.append(num)
            if len(out) == k:
                return out
