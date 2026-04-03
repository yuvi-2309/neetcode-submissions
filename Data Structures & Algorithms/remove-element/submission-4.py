class Solution:
        def removeElement(self, nums: List[int], val: int) -> int:
                arr = []

                for num in nums:
                    if val != num:
                        arr.append(num)
                                                    
                nums[:len(arr)] = arr
                return len(arr)