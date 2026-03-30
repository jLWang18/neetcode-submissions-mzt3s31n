class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = []
        for _ in range(len(nums) + 1):
            bucket.append([])

        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        for num, count in freq.items():
            bucket[count].append(num)
        
        out = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i] != []:
                for num in bucket[i]:
                    out.append(num)
            if len(out) == k:
                return out
