## 对角线遍历

解题思路：
分析后不难发现，第一条斜线下标和为0， 第二条斜线下标为1，第三条下标为2，最大下标和为 m + n - 2

故可以按照下标和生成字典，然后遍历字典取出结果，这个方法很好理解，需要注意的是，下标和为偶数时，需要将数组反转取出
```
if entry[0] % 2 == 0:
    [res.append(x) for x in entry[1][::-1]]
else:
    [res.append(x) for x in entry[1]]
```

另外一种方法则稍难理解一些，遍历最大和，按照对角线走势取出对应数据, 偶数时m递减n递增，奇数时m递增n递减，同时需要注意遍历完中间对角线时，m,n值需要变化：
```
class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        row, col = len(matrix), len(matrix[0])
        max_len = row+col
        result = []
        for k in range(max_len):
            m = n =0
            if k%2 == 0:
                
                if k < row: 
                    m = k
                    n = 0
                else: 
                    m = row-1
                    n = k-m
                while m>=0 and n<col:
                    result.append(matrix[m][n])
                    m -= 1
                    n += 1
            else:
                
                if  k < col: 
                    m = 0
                    n = k
                else: 
                    n = col - 1
                    m = k-n
                while n>=0 and m<row:
                    result.append(matrix[m][n])
                    m += 1
                    n -= 1
        return result
```