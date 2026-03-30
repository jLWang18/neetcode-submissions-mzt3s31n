class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            len_s = len(s)
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        i = 0
        while i < len(s):
            # get length before delimeter
            d = i
            while s[d] != "#":
                d += 1
            size = int(s[i:d])

            my_str = s[d+1: d + 1 + size]
            res.append(my_str)
            i = d + 1 + size
            
        return res
