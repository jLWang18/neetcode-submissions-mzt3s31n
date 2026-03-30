class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            out += str(len(s)) + "#" 
            for ch in s:
                out += ch
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i= 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            print(length)
            print(j+1)
            word = s[j + 1: j+ 1 + length]
            out.append(word)
            print(out)
            i = j + 1 + length
        return out

