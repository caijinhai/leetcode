#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        s_dict = {}
        res_str = ''
        for index, char in enumerate(s):
            if char not in s_dict.keys():
                s_dict[char] = [index]
            else:
                for i in s_dict[char]:
                    sub_str = s[i:index + 1]
                    if sub_str == sub_str[::-1]:
                        if not res_str:
                            res_str = sub_str
                        else:
                            if len(sub_str) > len(res_str):
                                res_str = sub_str

                s_dict[char].append(index)
        if not res_str:
            res_str = s[0]
        return res_str

if __name__ == "__main__":
    print(Solution().longestPalindrome("babadada"))
# @lc code=end

