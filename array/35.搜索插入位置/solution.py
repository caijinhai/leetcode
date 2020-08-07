# class Solution(object):
#     def searchInsert(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         find_index = -1
#         for index, val in enumerate(nums):
#             if val >= target:
#                 find_index = index
#                 break
#         if find_index == -1:
#             find_index = len(nums)
#         return find_index

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if nums[0] >= target:
            return 0
        if nums[-1] < target:
            return n
        left = 0
        right = n - 1
        find_index = -1
        while left <= right:
            center = int((right - left) / 2 + left)
            if nums[center] >= target:
                right = center - 1
                find_index = center
            else:
                left = center + 1
        return find_index 

if __name__ == "__main__":
    print(Solution().searchInsert([1,3, 5, 6], 2))