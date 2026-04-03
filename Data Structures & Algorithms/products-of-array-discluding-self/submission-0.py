class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums) 

        for i in range(len(nums)):
            for k in range(len(nums)):
                if i == k:
                    continue
                
                result[i] *= nums[k]

        return result