#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            else:
                if ("{0}{1}".format(stack[-1], c)) in ["()", "{}", "[]"]:
                    del stack[-1]
                else:
                    stack.append(c)
        return len(stack) == 0

print(Solution().isValid("()[]{}"))


# @lc code=end

