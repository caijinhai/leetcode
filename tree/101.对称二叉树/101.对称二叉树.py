#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        stack.append([root])
        is_symmetric = True
        while len(stack) > 0:
            nodes = stack.pop()
            values = []
            childs = []
            for node in nodes:
                if node:
                    values.append(node.val)
                    childs.append(node.left)
                    childs.append(node.right)
                else:
                    values.append(None)
            if values != values[::-1]:
                is_symmetric = False
                break
            if len(childs) > 0:
                stack.append(childs)
            
        return is_symmetric


class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        is_symmetric = True
        def jusitfy_symmetric(nodes):
            values = []
            childs = []
            for node in nodes:
                if node:
                    values.append(node.val)
                    childs.append(node.left)
                    childs.append(node.right)
                else:
                    values.append(None)
            if values != values[::-1]:
                is_symmetric = False
                return
            jusitfy_symmetric(childs)
        return is_symmetric

            


        
# @lc code=end

