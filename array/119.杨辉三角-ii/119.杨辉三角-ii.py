#
# @lc app=leetcode.cn id=119 lang=python
#
# [119] 杨辉三角 II
#

# @lc code=start
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        i = 0
        before = []
        arr = []
        while i <= rowIndex:
            if i < 2:
                before = [1 for _ in range(i+1)]
            else:
                arr = [1]
                for j in range(1, i):
                    arr.append(before[j-1] + before[j])
                arr.append(1)
                before = arr
            i += 1
        return before

if __name__ == "__main__":
    print(Solution().getRow(3))



# @lc code=end

