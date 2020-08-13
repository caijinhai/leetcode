## 旋转矩阵

解题思路：
复制一份数组，注意不能用 =，这种是引用传递
可以采用 copy.deepcopy() 或者重新构造新的二维数组
```
new_matrix = [[0] * n for _ in range(n)]
```

或者可以将二维数组转换成一维数组

转换关系：
```
new_matrix[j][n - i - 1] = matrix[i][j]
```

