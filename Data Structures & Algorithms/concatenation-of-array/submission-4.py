class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums;
        
        # Solution 2
        # list = [0] * (2 * len(nums))
        # for i, item in enumerate(nums):
        #     list[i] = list[i + len(nums)] = item

        # return list