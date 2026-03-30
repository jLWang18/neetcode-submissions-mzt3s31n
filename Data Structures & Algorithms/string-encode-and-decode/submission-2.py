class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # get length of s
            length = len(s)
            # convert to string
            length_str = str(length)

            # append string s to res with following signature: length of s#string s 
            res += length_str + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length_str = s[i:j]
            length = int(length_str)
            # the length tells us the length of the following string s
            my_str = s[j + 1: j + 1 + length]
            res.append(my_str)
            i = j + 1 + length
        return res
