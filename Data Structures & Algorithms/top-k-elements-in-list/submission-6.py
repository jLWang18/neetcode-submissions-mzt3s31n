class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dictionary to count freq of num
        count = {}
        # bucket sorting - initialize empty arr with same size as input nums arr
        freq = [[] for i in range(len(nums) + 1)]

        # keep record of occurence of num in count dict
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        # map ocurrence as index and num as val to freq array
        for n, c in count.items():
            freq[c].append(n)
        
        # get the top nums by looping the freq array backward
        res = []
        for i in range(len(freq) - 1, 0, -1):
            # loop the nums at freq[i]
            for num in freq[i]:
                res.append(num)
            # if reach the top k, return res array
            if len(res) == k:
                return res