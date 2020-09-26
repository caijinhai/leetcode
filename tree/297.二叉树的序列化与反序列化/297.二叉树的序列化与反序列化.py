#
# @lc app=leetcode.cn id=297 lang=python
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
import json
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return 'X,'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + ',' + left + right

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        res = data.split(',')

        def build_tree(res):
            root_val = res[0]
            del res[0]
            if root_val == 'X':
                return None
            root = TreeNode(int(root_val))
            root.left = build_tree(res)
            root.right = build_tree(res)
            return root
        return build_tree(res)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

