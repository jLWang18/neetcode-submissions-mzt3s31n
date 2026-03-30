class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isAlpha(ch):
            if "a" <= ch <= "z" or "A" <= ch <= "Z" or "0" <= ch <= "9":
                return True
            else:
                return False
        f = 0
        l = len(s) - 1
        while f < l:
            while not isAlpha(s[f]) and f < l:
                print("first index: " + str(f))
                f += 1
            while not isAlpha(s[l]) and f < l:
                print("last index: " + str(l))
                l -= 1

            print("compare between: " + str(f) + " and " + str(l))
            print("char first: " + s[f])
            print("c")
            if s[f].lower() != s[l].lower():
                return False
            f += 1
            l -= 1
        return True