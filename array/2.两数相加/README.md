## 两数相加

解题思路：
两数相加，就是对位数的相加，但是需要考虑到进位的处理，尤其是运行到最后时，如果还有进位，则需添加
其次，由于对象赋值，其实是对象的引用,不断传递对象的引用，输出链表
```
current = dummyHead

current.next = new Node()
current = current.next
```
