## 长度最小的子数组

解题思路：
right偏移位置先地址，当满足调节后，left偏移位置再递减，然后比较值大小

划动窗口问题：
伪代码如下
```
设置left, right
while right < length:
    sum += nums[right]
    while sum >= s:
        left += 1
        sum -= nums[left]
    right += 1
```

```
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 典型的滑动窗口题目
        length = len(nums)
        left,right = 0,0
        current_sum = 0
        min_len = length
        flag = False
        
        # 窗口开始向右扩张
        while(right<length):
            current_num = nums[right]
            current_sum += current_num
            while(current_sum>=s):
                # 判断是否是长度最小
                flag = True
                current_length = right-left+1
                min_len = min(current_length,min_len)
                # 收缩窗口
                current_sum -= nums[left]
                left += 1

            right += 1
        
        return min_len if flag==True else 0
```

划动窗口：
1. 左右指针同方向递增
2. 左右指针反方向靠近
一定要确定，左右指针运行方向，并且确定先后顺序，确定取值规则，然后再比较