## 116.填充每个节点的下一个右侧节点指针

1. 比较好理解的一种方式，将节点所有子节点放入栈内，循环遍历赋值next, 然后递归执行
2. 优化方案：使用while来进行隐藏式递归
```
class Solution:
    def connect(self,root:'Node'):
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root

```