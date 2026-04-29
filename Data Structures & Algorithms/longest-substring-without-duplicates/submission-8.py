class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        left, right = 0, 0
        length = 0
        while right < len(s):
            while s[right] in my_set:
                my_set.remove(s[left])
                left += 1
            my_set.add(s[right])
            length = max(length, right - left + 1)
            right += 1
        return length