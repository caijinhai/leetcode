#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = collections.deque()
        stack.append([root])
        res = []
        while stack:
            nodes = stack.popleft()
            items = []
            child = []
            for node in nodes:
                if node:
                    items.append(node.val)
                    if node.left:
                        child.append(node.left)
                    if node.right:
                        child.append(node.right)
            if len(child) > 0:
                stack.append(child)
            if len(items) > 0:
                res.append(items)
        return res

# @lc code=end

