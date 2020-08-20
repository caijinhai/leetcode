## 设计循环队列

解题思路：
1. 维护队列数组，queue = []
2. 维护head, tail指针
3. 维护队列容量 size

判断队列空：如果为空便把头尾指针设为 -1，所以判空的条件就是 head,tail 同时为-1
判断队列满：有两种情况，一种是 tail - head = size -1；
另外一种情况是 head - tail = 1


还有另外一种实现思路：
维护一个指针p_start, 当同时记录 容量size 和 队列count两个值