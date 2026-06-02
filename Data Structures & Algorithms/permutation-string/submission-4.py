class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       # edge case: diffrent length
       if len(s1) > len(s2):
            return False
       
       # initialize two arrays to compare characters (for the first s1 length)
       s1Count, s2Count = [0] * 26, [0] * 26
       for i in range(len(s1)):
        # fill s1 chars with its frequency in s1Count array
        s1Count[ord(s1[i]) - ord('a')] += 1
        # fill s2 chars with its frequency in s2Count array
        s2Count[ord(s2[i]) - ord('a')] += 1

       # initialize this variable to compare counts (for the first s1 length)
       matches = 0
       # there are 26 alphabets
       for i in range(26):
        # case 1: if matches, then increment matches. Else, we don't increment
        if s1Count[i] == s2Count[i]:
            matches += 1
       
       # compare chars and counts for the next s1 length and the next s1 length after that
       left = 0
       for right in range(len(s1), len(s2)):
        if matches == 26:
            return True
            
        # map char in s2 in s2Count array
        index = ord(s2[right]) - ord('a')
        s2Count[index] += 1
        # if the frequency matches with s1Count, then increment matches
        if s1Count[index] == s2Count[index]:
            matches += 1
        # if the frequency is too large by 1, then decrement matches.
        # Before the frequency is equal, now the frequency is 
        elif s1Count[index] + 1 == s2Count[index]:
            matches -= 1
            
        index = ord(s2[left]) - ord('a')
        s2Count[index] -= 1
        if s1Count[index] == s2Count[index]:
            matches += 1
        elif s1Count[index] - 1 == s2Count[index]:
            matches -= 1
            
        # increment left ptr
        left += 1
      
       return matches == 26

