#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        values = []
        def do_traversal(node):
            if node:
                do_traversal(node.left)
                do_traversal(node.right)
                values.append(node.val)
        do_traversal(root)
        return values


import collections
class Solution2(object):

    def postorderTraversal(self, root):
        stack = collections.deque()
        stack.append(root)
        values = []
        while stack:
            node = stack.pop()
            values.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return values[::]

            
                

# @lc code=end

