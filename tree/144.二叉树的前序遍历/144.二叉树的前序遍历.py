#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.values = []
        self.pre_order_traversal(root)
        return self.values

    def pre_order_traversal(self, node):
        if node:
            self.values.append(node.val)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)
        

import collections
class Solution2(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        values = []
        pNode = root
        stack = []
        while pNode or len(stack) > 0:
            if pNode:
                values.append(pNode.val)
                stack.append(pNode.right)
                stack.append(pNode.left)
                pNode = stack.pop()
            else:
                pNode = stack.pop()
        return values


def arr_to_tree(arr):
    queue = []
    root = TreeNode(arr[0])
    queue.append(root)
    i = 1
    total = len(arr)
    while i < total:
        pNode = queue.pop()
        if i < total and arr[i] is not None:
            pNode.left = TreeNode(arr[i])
            queue.append(pNode.left)
        i += 1
        if i < total and arr[i] is not None:
            pNode.right = TreeNode(arr[i])
            queue.append(pNode.right)
        i += 1
    return root

if __name__ == "__main__":
    root = arr_to_tree([1, 2, 3, 4, 5, None, 7])
    print(Solution().preorderTraversal(root))
    print(Solution2().preorderTraversal(root))

# @lc code=end

