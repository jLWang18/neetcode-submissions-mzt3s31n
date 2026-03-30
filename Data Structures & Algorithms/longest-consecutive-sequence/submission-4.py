class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            # if start of sequence (i.e., no left number)
            if not (num - 1) in numSet:
                # increment length while there's a next number
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
        