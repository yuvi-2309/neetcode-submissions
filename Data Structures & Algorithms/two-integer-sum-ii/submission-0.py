class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for l in range(len(numbers)):
            for r in range(len(numbers)):
                if numbers[l] + numbers[r] == target:
                    return [l + 1, r + 1]
                
        return [0, 0]