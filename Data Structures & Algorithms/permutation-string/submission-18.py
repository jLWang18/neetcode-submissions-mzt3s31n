class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        a1, a2 = [0] * 26, [0] * 26
        matches = 0
        for i in range(len(s1)):
            a1[ord(s1[i]) - ord("a")] += 1
            a2[ord(s2[i]) - ord("a")] += 1
        
        for i in range(26):
            if a1[i] == a2[i]:
                matches += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # shift left
            # dcrement freq
            index = ord(s2[left]) - ord("a")
            a2[index] -= 1
            if a1[index] == a2[index]:
                matches += 1
            elif a1[index] - 1 == a2[index]:
                matches -= 1
            left += 1

            #count right
            index = ord(s2[right]) - ord("a")
            a2[index] += 1
            if a1[index] == a2[index]:
                matches += 1
            elif a1[index] + 1 == a2[index]:
                matches -= 1
        return matches == 26 
            
