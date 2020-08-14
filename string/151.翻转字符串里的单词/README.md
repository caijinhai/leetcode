## 翻转字符串里的单词

解题思路：
去掉两边的空格，按空格拆分成数据再翻转合成即可

一个两行代码解决问题：
```
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        return " ".join(s.split()[::-1])
```