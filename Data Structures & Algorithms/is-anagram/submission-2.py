class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        #using hashmaps (storing frequency of each letter)

        s_map = {}
        t_map = {}

        for i in s:
            s_map[i] = s_map.get(i, 0) + 1

        for i in t:
            t_map[i] = t_map.get(i, 0) + 1

        
        for key in s_map:
            if s_map[key] != t_map.get(key, 0):
                return False
        
        return True



        

        