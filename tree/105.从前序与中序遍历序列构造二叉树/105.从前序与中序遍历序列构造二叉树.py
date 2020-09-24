#
# @lc app=leetcode.cn id=105 lang=python
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        def do_build_tree(pres, ins):
            if len(pres) == 0 or len(ins) == 0:
                return None
            node = TreeNode(pres[0])
            index = ins.index(node.val)
            node.left = do_build_tree(pres[1:index+1], ins[:index])
            node.right = do_build_tree(pres[index+1:], ins[index+1:])
            return node
        return do_build_tree(preorder, inorder)

if __name__ == "__main__":
    print(Solution().buildTree([3,9,20,15,7], [9,3,15,20,7]))

# @lc code=end

