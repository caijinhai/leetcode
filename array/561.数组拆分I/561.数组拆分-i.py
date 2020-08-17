#
# @lc app=leetcode.cn id=561 lang=python
#
# [561] 数组拆分 I
#

# @lc code=start
class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = int(len(nums) / 2)
        nums.sort()
        sum = 0
        for i in range(n):
            sum += nums[2 * i]
        return sum


if __name__ == "__main__":
    print(Solution().arrayPairSum([1,4,3,2]))
        
# @lc code=end

