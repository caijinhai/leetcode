## 最长公共前缀

解题思路：
获取字符串里面最短的，遍历拼接字串，看是否都在所有字符串中

更牛逼的思路：
取字符串中的最小值和最大值，因为字串最小最大值是按照字母的排序来的
只需比较最小最大值重复的字串有哪些
```
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        str0 = min(strs)
        str1 = max(strs)
        n = len(str0)
        for i in range(n):
            if str0[i]!=str1[i]:
                return str0[:i]
        return str0
```