#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        if len(numbers) == 0:
            return [0,0]
        if target < numbers[0]:
            return [0,0]
        index = [0,0]
        dicts = {}
        for i in range(n):
            if (target - numbers[i]) in dicts.keys():
                index = [dicts.get(target - numbers[i]) + 1, i+1]
            else:
                dicts.setdefault(numbers[i], i)
        return index

if __name__ == '__main__':
    print(Solution().twoSum([2, 7, 11, 15], 9))
                


# @lc code=end

