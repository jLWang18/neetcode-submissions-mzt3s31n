class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hashmap for 
        my_dict = defaultdict(list)

        # loop each input string
        for s in strs:
            # create count array lowercase (a-z)
            count = [0] * 26
            # loop each char in input sting
            for ch in s:
                # update the occurrence of char
                count[ord(ch) - ord("a")] += 1
            # add count array to dict as key and input string as value     
            my_dict[tuple(count)].append(s)
        
        # convert to list
        return list(my_dict.values())
            
        