class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlpha(ch):
            if "0" <= ch <= "9" or "a" <= ch <= "z" or "A" <= ch <= "Z":
                return True

        left = 0
        right = len(s) - 1

        while left < right:
            # we need to check if it is alphanumeric
            # if not, we need to increment left and decrement right
            while left < right and not isAlpha(s[left]):
                left += 1
            
            while left < right and not isAlpha(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True