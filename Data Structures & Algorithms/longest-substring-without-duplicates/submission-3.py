class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        sub = set()
        longest = 0
        while right < len(s):
            while s[right] in sub:
                sub.remove(s[left])
                left += 1
            sub.add(s[right])
            length = (right - left) + 1
            longest = max(longest, length)
            right += 1
        return longest