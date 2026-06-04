class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        # same chars, same counts
        s1Count, s2Count = [0] * 26, [0] * 26
        matches = 0
        # first window
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        # determine number of matches
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                matches += 1
       
        print(matches)
        # continue to slide the window
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            # remove the left char
            # decrement char freq
            s2Count[ord(s2[left]) - ord('a')] -= 1
            # update the matches
            if s1Count[ord(s2[left]) - ord('a')] == s2Count[ord(s2[left]) - ord('a')]:
                matches += 1
            elif s1Count[ord(s2[left]) - ord('a')] - 1 == s2Count[ord(s2[left]) - ord('a')]:
                matches -= 1 
            
            print("matches after we remove left char: " + str(matches))

            # add new right char
            s2Count[ord(s2[right]) - ord('a')] += 1
            if s1Count[ord(s2[right]) - ord('a')] == s2Count[ord(s2[right]) - ord('a')]:
                matches += 1
            elif s1Count[ord(s2[right]) - ord('a')] + 1 == s2Count[ord(s2[right]) - ord('a')]:
                matches -= 1

            left += 1
            
        return matches == 26
        
