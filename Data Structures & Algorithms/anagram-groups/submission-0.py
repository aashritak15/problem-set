from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         
        strs_dict = defaultdict(list) 

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            strs_dict[key].append(word) 

        
        return list(strs_dict.values())
        