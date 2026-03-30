class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlpha(ch):
            if "0" <= ch <= "9" or "A" <= ch <= "Z" or "a" <= ch <= "z":
                return True
            else:
                return False
        i = 0
        j = len(s) - 1
        while i < j:
            print(isAlpha(s[i]))
            print(isAlpha(s[j]))
            while not isAlpha(s[i]) and i < j:
                i += 1
            while not isAlpha(s[j]) and i < j:
                print("here")
                j -= 1
            print(i)
            print(j)
            
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

