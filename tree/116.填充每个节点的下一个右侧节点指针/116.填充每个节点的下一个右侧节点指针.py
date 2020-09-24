#
# @lc app=leetcode.cn id=116 lang=python
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        def do_connect(nodes):
            stack = []
            childs = []
            for node in nodes:
                if node.left:
                    stack.append(node.left)
                    childs.append(node.left)
                if node.right:
                    stack.append(node.right)
                    childs.append(node.right)
            next = None
            while stack:
                pre = stack.pop()
                pre.next = next
                next = pre
            if len(childs) > 0:
                do_connect(childs)
        root.next = None
        do_connect([root])
        return root

        
# @lc code=end

