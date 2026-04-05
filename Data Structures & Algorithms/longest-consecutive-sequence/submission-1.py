class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0

        # bad solution, runs multiple times O(n^3)
        # for n in nums:
        #     length = 1

        #     while n + length in nums:
        #         length += 1
            
        #     longest = max(length, longest)

        # Optimal
        numSet = set(nums)
        for num in nums:
            if num - 1 not in numSet:
                length = 1

                while num + length in numSet:
                    length += 1

                longest = max(length, longest)
        
        return longest
