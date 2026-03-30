class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        for s in strs:
            word_len = len(s)
            out += str(word_len) + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        print(s)
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            print(j)
            count = int(s[i:j])
            word = s[j+1: count + j +1]
            out.append(word)
            print(out)
            i = count + j + 1
            print("i now " + str(i))
        return out

