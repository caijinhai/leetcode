# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        values = []

        def do_traversal(node):
            if node:
                do_traversal(node.left)
                values.append(node.val)
                do_traversal(node.right)
        do_traversal(root)
        return values

import collections
class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        pNode = root
        stack = collections.deque()
        values = []
        while pNode or len(stack) > 0:
            while pNode:
                stack.append(pNode)
                pNode = pNode.left
            pNode = stack.pop()
            values.append(pNode.val)
            pNode = pNode.right
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
    print(Solution2().inorderTraversal(arr_to_tree([1,None,2,3])))