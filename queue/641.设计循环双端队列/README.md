## 设置循环双端队列

1. 双端队列，由于是两边删除两边插入，注意容量+1
2. tail指向下一个插入位置
3. 插入一个是先赋值后调整偏移位置，一个是先调整偏移位置后赋值