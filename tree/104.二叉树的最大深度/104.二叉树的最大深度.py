#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1


class Solution2(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.answer = 0
        def do_max_depth(node, depth=1):
            if not node:
                return
            if not node.left and not node.right:
                self.answer = max(self.answer, depth)
            do_max_depth(node.left, depth+1)
            do_max_depth(node.right, depth+1)
        do_max_depth(root, 1)
        return self.answer




# @lc code=end

