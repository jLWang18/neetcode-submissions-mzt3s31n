class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = defaultdict(list)

        for s in strs:
            arr = [0] * 26
            for ch in s:
                index = ord(ch) - ord("a")
                arr[index] += 1
            my_dict[tuple(arr)].append(s)
        
        out = []
        for _, arr in my_dict.items():
            my_list = []
            for s in arr:
                my_list.append(s)
            out.append(my_list)
        return out
            #print(my_dict.values)
        #return [my_dict.values]
