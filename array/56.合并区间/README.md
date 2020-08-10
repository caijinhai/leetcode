## 合并区间

解题思路：
先按照子数组第一个元素排序
再标记merged数组最后一个子数组末尾大小和后一个元素比较
```
if not merged or merged[-1][1] < interval[0]:
    merged.append(interval)
else:
    merged[-1][1] = max(merged[-1][1], interval[1])
```