#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
from typing import List

class Solution(object):
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        def inOrderTraverse1(cur):
            if cur:
                inOrderTraverse1(cur.left)
                res.append(cur.val)
                inOrderTraverse1(cur.right)

        inOrderTraverse1(root)
        return res

class Solution2(object):
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = collections.deque()
        pNode = root
        res = []
        while pNode or stack:
            if pNode:
                stack.append(pNode)
                pNode = pNode.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                pNode = cur.right

        return res


def arr_to_tree(arr):
    if not arr:
        return None

    tree = collections.deque()
    root = TreeNode(arr[0])
    tree.append(root)
    i = 1
    while i < len(arr):
        cur = tree.popleft()
        if not cur:
            continue
        if i < len(arr):
            if arr[i] == 'null':
                left = None
            else:
                left = TreeNode(arr[i])
            cur.left = left
            i += 1
        if left:
            tree.append(left)
        if i < len(arr):
            if arr[i] == 'null':
                right = None
            else:
                right = TreeNode(arr[i])
            cur.right = right
            i += 1
        if right:
            tree.append(right)
    return root


tree = arr_to_tree([1,'null',2,3])
print(tree.left)
print(tree.right.val)
print(tree.right.left.val)
print(tree.right.left.left)
print(Solution2().inorderTraversal(tree))

# @lc code=end

