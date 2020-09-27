from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        if len(nums) < 2:
            return len(nums)
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
                j += 1
        return i+1
    