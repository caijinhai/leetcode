#
# @lc app=leetcode.cn id=151 lang=python
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        words = []
        for word in s.split(' '):
            if word:
                words.append(word)
        words.reverse()
        res_s = ' '.join(words)
        return res_s

if __name__ == "__main__":
    print(Solution().reverseWords("a good   example"))
            
# @lc code=end

