## 两数之和-输入有序数组

解题思路：
1. 可以根据建立值-index的字典，判断target - numbers[i]值是否在字典中
2. 建立left, right双指针，判断位置左右两位置值之和和target比较，左递增或右递增
3. target - numbers[i] 值二分查找