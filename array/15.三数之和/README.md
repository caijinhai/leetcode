## 三数之和

解题思路：
和两数之和一样，都是通过锁定一个值后，查找target=(0 - firtst)
但和两数之和不一样的是，循环要多一层，且因为是三个数，需要在处理过程中，第二个数若和第一个数相同时，在处理完第一遍时跳过
`if first > 0 and nums[first] == nums[first - 1]:`
`if second > first + 1 and nums[second] == nums[second - 1]:`

通过先把数组排序： nums.sort()
来减少重复