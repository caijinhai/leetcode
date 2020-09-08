#
# @lc app=leetcode.cn id=150 lang=python
#
# [150] 逆波兰表达式求值
from typing import List

# @lc code=start
class Solution(object):
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """

        operaters = ['+', '-', '*', '/']
        stack = []
        res = 0

        for char in tokens:
            if char not in operaters:
                stack.append(int(char))
                res = int(char)
            else:
                a = stack.pop()
                b = stack.pop()
                if char == '+':
                    val = a + b
                if char == '-':
                    val = b - a
                if char == '*':
                    val = a * b
                if char == '/':
                    val = int(b / a)
                stack.append(val)
                res = val
            # print(stack)
        return res


if __name__ == "__main__":
    print(Solution().evalRPN(["18"]))
# @lc code=end

