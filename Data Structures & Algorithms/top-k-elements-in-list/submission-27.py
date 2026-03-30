class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for _ in range(len(nums) + 1)]
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        for num, occur in freq.items():
            arr[occur].append(num)
        
        out = []
        for i in range(len(arr) -1, -1, -1):
            if arr[i] != None:
                for num in arr[i]:
                    out.append(num)
            if len(out) == k:
                return out