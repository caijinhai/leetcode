## 运用递归解决树的问题

### 自顶向下
确定一些参数，从该节点自身解决出发寻找答案
可以使用这些参数和节点本身的值来决定什么应该是传递给它子节点的参数
* 原理：
```
return specific value for null node
update the answer if needed
left_ans = top_down(root.left, left_params)
right_ans = top_down(root.right, right_params)
return the answer if needed
```

* 例如：
```
return if root is null
if root is a leaf node:
  answer = max(answer, depth)
maximum_depth(root.left, depth+1)
maximum_depth(root.right, depth+1)
```

* code example
```
answer = 0
def maximum_depth(root, depth=1):
  if not root:
    return
  if not root.left and not root.right:
    answer = max(answer, depth)
  maximum_depth(root.left, depth+1)
  maximum_depth(root.right, depth+1)

maximum_depth(root, depth=1)
return answer
```

### 自底向上
对于树中的任意一个节点，如果你知道它子节点的答案，你能计算出该节点的答案
* 原理：
```
return specific value for null node
left_ans = bottom_up(root.left)
right_ans = bottom_up(root.right)
return answers  // answer <-- left_ans, right_ans, root.val
```

* 例如：
```
return 0 if root is null
left_depth = maximum_depth(root.left)
right_depth = maximum_depth(root.right)
return max(left_depth, right_depth) + 1
```

* code example:
```
def maximum_depth(root):
  if not root:
    return 0
  left_depth = maximum_depth(root.left)
  right_depth = maximum_depth(root.right)
  return max(left_depth, right_depth) + 1
```