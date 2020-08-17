## 最大连续1的个数

解题思路：
遍历，若==1 则res += 1,否则 res = 0
在res == 1时，比较res值与max最大值比较，取最大值
```
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num=0
        res=0
        for i in nums:
            if i==1:
                res+=1
                if res>max_num:
                    max_num=res
            else:
                res=0
        return max_num
```