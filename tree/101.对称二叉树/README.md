## 101.对称二叉树

1. 迭代法，子节点数组入栈，判断节点值数组values == values[::-1]
2. 递归法，判断子节点数组是否对称，将上一层节点数组传入下一层递归中