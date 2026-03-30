class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(ch):
            if "a" <= ch <= "z" or "A" <= ch <= "Z" or "0" <= ch <= "9":
                return True
            else:
                return False
        left = 0
        right = len(s) - 1
        while left < right:
            while not check(s[left]) and left < right:
                left += 1
            while not check(s[right]) and left < right:
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True  