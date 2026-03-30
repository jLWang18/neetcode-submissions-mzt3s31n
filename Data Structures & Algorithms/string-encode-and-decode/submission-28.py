class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for word in strs:
            out += str(len(word)) + "#" + word
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            word = s[j+1: j+1+count]
            out.append(word)
            i = j+1+count
        return out