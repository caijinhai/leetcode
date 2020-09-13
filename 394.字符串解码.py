#
# @lc app=leetcode.cn id=394 lang=python
#
# [394] 字符串解码
#

# @lc code=start
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = []
        i = 0
        total = len(s)
        while i < total or len(stack) > 0:
            if s[i] == '[':
                stack.append((s[i-1], i))
            elif s[i] == ']':
                n, j = stack[-1]
                del stack[-1]
                sss = n * s[j+1:i+1]
                res.append(sss)
            else:
                res.append(s[i])
        return ''.join(res)


if __name__ == "__main__":
    print(Solution().decodeString("3[a]2[bc]"))

# @lc code=end

