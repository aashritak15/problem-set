class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #using a hashset 

        nums_set = set()

        for n in nums:
            if n in nums_set:
                return True

            nums_set.add(n)
        
        return False

        




