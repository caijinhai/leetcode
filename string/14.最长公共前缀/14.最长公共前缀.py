#
# @lc app=leetcode.cn id=14 lang=python
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        strs.sort(key=lambda item: len(item))
        prefix = ''
        for char in strs[0]:
            prefix += char
            has_prefix = True
            for item in strs:
                if not item.startswith(prefix):
                    has_prefix = False
            if not has_prefix:
                prefix = prefix[:-1]
        return prefix



if __name__ == "__main__":
    Solution().longestCommonPrefix(["flower","flow","flight"])

# @lc code=end

