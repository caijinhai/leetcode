#
# @lc app=leetcode.cn id=112 lang=python
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.is_has = False
        if not root:
            return False

        def do_has_path_sum(node, val):
            if not node.left and not node.right:
                if (val + node.val) == sum:
                    self.is_has = True
                return
            if node.left:
                do_has_path_sum(node.left, val + node.val)
            if node.right:
                do_has_path_sum(node.right, val + node.val)
        do_has_path_sum(root, 0)
        return self.is_has

# @lc code=end

