#
# @lc app=leetcode.cn id=557 lang=python
#
# [557] 反转字符串中的单词 III
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        arr = []
        for word in words:
            arr.append(word[::-1])
        return ' '.join(arr)

if __name__ == "__main__":
    print(Solution().reverseWords("Let's take LeetCode contest"))

# @lc code=end

