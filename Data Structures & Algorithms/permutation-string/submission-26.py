class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1a, s2a = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1a[ord(s1[i]) - ord("a")] += 1
            s2a[ord(s2[i]) - ord("a")] += 1
        
        match = 0
        for i in range(26):
            if s1a[i] == s2a[i]:
                match += 1
        
        print("initial match = " + str(match))
        left = 0
        for right in range(len(s1), len(s2)):
            if match == 26:
                return True

            # shift left ptr
            index = ord(s2[left]) - ord("a")
            s2a[index] -= 1
            if s1a[index] == s2a[index]:
                match += 1
            elif s1a[index] - 1 == s2a[index]:
                match -= 1
            left += 1

            print("After shifting left, match = " + str(match))
            
            # add right
            index = ord(s2[right]) - ord("a")
            s2a[index] += 1
            if s1a[index] == s2a[index]:
                match += 1
            elif s1a[index] + 1 == s2a[index]:
                match -= 1
            
            print("After shifting right, match = " + str(match))
        
        return match == 26

