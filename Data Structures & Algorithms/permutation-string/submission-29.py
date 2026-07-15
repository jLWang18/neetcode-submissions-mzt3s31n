class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        # same letters & freq
        s1A, s2A = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1A[ord(s1[i]) - ord("a")] += 1
            s2A[ord(s2[i]) - ord("a")] += 1

        match = 0
        for i in range(26):
            if s1A[i] == s2A[i]:
                match += 1

        left = 0
        for right in range(len(s1), len(s2)):
            if match == 26:
                return True
            # shift left
            index = ord(s2[left]) - ord("a")
            s2A[index] -= 1
            if s1A[index] == s2A[index]:
                match += 1
            elif s1A[index] - 1 == s2A[index]:
                match -= 1
            left += 1

            # shift right
            index = ord(s2[right]) - ord("a")
            s2A[index] += 1
            if s1A[index] == s2A[index]:
                match += 1
            elif s1A[index] + 1 == s2A[index]:
                match -= 1
        return match == 26
