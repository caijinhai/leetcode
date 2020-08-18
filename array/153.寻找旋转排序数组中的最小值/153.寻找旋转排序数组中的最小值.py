#
# @lc app=leetcode.cn id=153 lang=python
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[index]:
                return nums[i]
            else:
                index += 1
        return nums[0]

if __name__ == "__main__":
    print(Solution().findMin([1,2]))
    

# @lc code=end

