#
# @lc app=leetcode.cn id=485 lang=python
#
# [485] 最大连续1的个数
#

# @lc code=start
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        n = len(nums)
        max = 0
        for i in range(n):
            if nums[i] != 1:
                if (i - slow) > max:
                    max = i - slow
                slow = i + 1

        if slow != n and nums[-1] != 0:
            if (n - slow) > max:
                max = n - slow
        return max

if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([1,1,0,1]))
# @lc code=end

