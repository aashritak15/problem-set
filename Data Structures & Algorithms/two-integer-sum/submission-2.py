class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            starter = nums[i]
            complement = target - starter

            if complement in nums[i+1:]:
                j = nums[i+1:].index(complement) + i + 1
                return [i,j]
        