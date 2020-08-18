#
# @lc app=leetcode.cn id=118 lang=python
#
# [118] 杨辉三角
#

# @lc code=start
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr = []
        for i in range(1, numRows+1):
            if i <= 2:
                cur = [1 for _ in range(i)]
                arr.append(cur)
            else:
                cur = [1]
                for j in range(1, i-1):
                    cur.append(arr[i-2][j-1] + arr[i-2][j])
                cur.append(1)
                arr.append(cur)
        return arr

if __name__ == "__main__":
    print(Solution().generate(5))
            

            
# @lc code=end

