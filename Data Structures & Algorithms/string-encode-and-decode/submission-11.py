class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            size = len(s)
            out += str(size) + "#" + s
        return out
    def decode(self, s: str) -> List[str]:
        out = []
        print(s)
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            print(size)
            word = s[(j+1): j + size + 1]
            out.append(word)
            i = j + size + 1
            print(out)
            print(i)
            print(j)
        return out
