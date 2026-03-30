class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for s in strs:
            # arr from a-z
            count = [0] * 26
            for ch in s:
                # increment freq of ch in count array
                count[ord(ch) - ord("a")] += 1

            # covert to tuple
            my_dict[tuple(count)].append(s)
        
        return list(my_dict.values())

