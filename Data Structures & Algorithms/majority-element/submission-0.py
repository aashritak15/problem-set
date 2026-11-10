from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        boundary = len(nums) / 2
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        for num,count in counts.items():
            if(count > boundary):
                return num
        
        


        
        