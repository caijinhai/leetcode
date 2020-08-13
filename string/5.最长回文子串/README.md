## 最长回文子串

解题思路：回文串满足的条件是头和末尾的字母是相同的
所以可以通过遍历字符串以字母为key,建立字典，存在则找到相应左右位置取出字符串，并判断字符串是不是回文串

优化思路：
回文串只存在两中类型：
aba
abba
所以按照遍历当前index为开始节点，往两边发散，寻找是不是回文串，满足条件则继续往两本查找
```
def longestPalindrome(self, s):
    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res
 
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]
```