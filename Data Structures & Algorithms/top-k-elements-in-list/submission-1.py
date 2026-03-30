class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        arr = []
        for key, value in freq.items():
            heapq.heappush(arr, (value, key))
            if len(arr) > k:
                heapq.heappop(arr)
        
        out = []
        for _ , key in arr:
            out.append(key)
        return out
