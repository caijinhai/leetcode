#
# @lc app=leetcode.cn id=498 lang=python
#
# [498] 对角线遍历
#

# @lc code=start
class Solution(object):
    def findDiagonalOrder(self, matrix):
        d = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if (i+j) in d.keys():
                    d[i+j].append(matrix[i][j])
                else:
                    d[i+j] = [matrix[i][j]]
                
        res = []
        for entry in d.items():
            print(entry)
            if entry[0] % 2 == 0:
                [res.append(x) for x in entry[1][::-1]]
            else:
                [res.append(x) for x in entry[1]]
        
        return res


if __name__ == "__main__":
    Solution().findDiagonalOrder([
 [ 1, 2, 3],
 [ 4, 5, 6],
 [ 7, 8, 9]
])
        
# @lc code=end


# [0,0] Y+1
# [0,1] [1,0] x+1
# [2,0] [1,1] [0,2] x+1
# [1,2] [2,1] y+1
# [2,2]