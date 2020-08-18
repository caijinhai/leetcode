#
# @lc app=leetcode.cn id=283 lang=python
#
# [283] 移动零
#

# @lc code=start
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        slow = 0
        fast = 0

        while fast < len(nums):
            if nums[fast] == 0:
                fast += 1
            else:
                a = nums[slow] 
                nums[slow] = nums[fast]
                nums[fast] = a
                fast += 1
                slow += 1
        return nums


if __name__ == "__main__":
    print(Solution().moveZeroes([1]))
            


# @lc code=end

