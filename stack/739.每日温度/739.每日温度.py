#
# @lc app=leetcode.cn id=739 lang=python
#
# [739] 每日温度
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        res = [0] * len(T)
        stack = []

        for i in range(len(T)):
            tmp = T[i]
            while stack and tmp > T[stack[-1]]:
                pre_index = stack.pop()
                res[pre_index] = i - pre_index
            stack.append(i)
            print(stack)
        return res
            
print(Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))


# @lc code=end

