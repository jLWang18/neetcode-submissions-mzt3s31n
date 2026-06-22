class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        freq = {}
        left = 0
        for right in range(len(s)):
            freq[s[right]] = 1 + freq.get(s[right], 0)
            while ((right - left + 1) - max(freq.values()) > k):
                freq[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest