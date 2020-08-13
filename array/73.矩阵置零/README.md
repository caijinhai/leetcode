## 矩阵置零

解题思路：
遍历矩阵，找到矩阵中值为0的X轴或者Y轴
再次遍历，若轴在X或Y数组中则重置为0
```
class Solution(object):
    def setZeroes(self, matrix):
        if not matrix:
            return []
        m , n = len(matrix) , len(matrix[0])
        row_set , col_set = set() , set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row_set.add(i)
                    col_set.add(j)
        for row in row_set:
            for j in range(n):
                matrix[row][j] = 0
        for col in col_set:
            for i in range(m):
                matrix[i][col] = 0
        return matrix
```