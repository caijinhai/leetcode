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
        i = 0
        nums = []
        while i < len(s) or len(stack) > 0:
            if s[i].isdigit():
                nums.append(s[i])
            elif s[i] == '[':
                n = int(''.join(nums))
                stack.append((n, i, len(nums)))
                nums = []
            elif s[i] == ']':
                n, j, b = stack[-1]
                del stack[-1]
                sss = n * s[j+1:i]
                a = i - len(s)
                s = s[:j-b] + sss + s[i+1:]
                i = a + len(s)
            else:
                pass
            i = i + 1
        return s


if __name__ == "__main__":
    print(Solution().decodeString("3[a10[bc]]"))

# @lc code=end

