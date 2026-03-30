class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two dict for s and t
        # if freq of occurrence is the same, return True
        if len(s) != len(t):
            return False

        dict_s = {}
        for ch in s:
            if ch in dict_s:
                dict_s[ch] += 1
            else:
                dict_s[ch] = 1
        
        dict_t = {}
        for ch in t:
            if ch in dict_s and ch not in dict_t:
                dict_t[ch] = 1
            elif ch in dict_s and ch in dict_t:
                dict_t[ch] += 1
            else:
                return False
        
        for key, val in dict_s.items():
            if dict_s[key] != dict_t[key]:
                return False
        return True
        