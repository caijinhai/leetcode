#
# @lc app=leetcode.cn id=27 lang=python
#
# [27] 移除元素
#

# @lc code=start
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        slow = 0
        for i in range(len(nums)):
            if nums[i] != val:
                a = nums[slow]
                nums[slow] = nums[i]
                nums[i] = a
                slow += 1
        return slow


if __name__ == "__main__":
    print(Solution().removeElement([0,1,2,2,3,0,4,2], 2))
            
# @lc code=end

