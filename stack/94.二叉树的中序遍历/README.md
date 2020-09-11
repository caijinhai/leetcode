## 94.二叉树的中序遍历

二叉树四种主要遍历思想：
前序遍历：根结点 ---> 左子树 ---> 右子树

中序遍历：左子树---> 根结点 ---> 右子树

后序遍历：左子树 ---> 右子树 ---> 根结点

层次遍历：只需按层次遍历即可

根据思想写出递归方程：
```
def inOrderTraverse1(cur):
    if cur:
        inOrderTraverse1(cur.left)
        print(cur.val)
        inOrderTraverse1(cur.right)
```

用栈方式实现，要考虑父节点：
父节点不为空，则入栈，pNode = pNode.left
父节点为空，则出栈，打印值，pNode = pNode.right
