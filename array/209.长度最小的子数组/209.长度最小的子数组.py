#
# @lc app=leetcode.cn id=209 lang=python
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        n = len(nums)
        sum = 0
        c = 0
        max = 0
        while c <= n:
            sum = 0
            for i in range(c, len(nums)):
                sum += nums[i]
                if sum >= s:
                    print(c, i, sum)
                    if max == 0:
                        max = i - c + 1
                    else:
                        if (i - c + 1) < max:
                            max = i - c + 1
                    break
            c += 1
        return max

        

if __name__ == "__main__":
    print(Solution().minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]))
        
# @lc code=end

