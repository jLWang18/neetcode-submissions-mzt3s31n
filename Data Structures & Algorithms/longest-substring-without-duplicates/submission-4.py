class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = set()
        left = 0
        right = 0
        length = 0
        while right < len(s):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1
            sub.add(s[right])
            length = max(length, right - left + 1)
            right += 1
        return length