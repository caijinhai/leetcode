## 队列实现

解题思路：
1. 用一个指针p_start记录当前队列头位置
2. 判断队列是否为空，p_start >= queue.size()

缺点：
在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间