## 733.图像渲染

1. 读懂题意，在二维数组中，若与给定位置的值相等，则需要重新赋值为新的值即可
2. 需要判断是否已经处理过该节点，否则就会陷入死循环中
3. 故而用栈思想来解决，广度优先搜索思想