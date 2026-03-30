class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlpha(ch):
            if 'a' <= ch <= 'z' or 'A' <= ch <= 'Z' or '0' <= ch <= '9':
                return True
            else:
                return False

        start = 0
        end = len(s) - 1
        while start < end:
            print("start: " + s[start])
            print("end: " + s[end])
            while not isAlpha(s[start]) and start < end:
                start += 1
            while not isAlpha(s[end]) and start < end:
                end -= 1
            
            print(start)
            print
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
            print(start)
            print(end)
        return True