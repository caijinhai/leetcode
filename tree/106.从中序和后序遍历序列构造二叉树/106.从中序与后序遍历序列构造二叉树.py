#
# @lc app=leetcode.cn id=106 lang=python
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def do_build_tree(inn, post):
            if len(inorder) == 0 or len(post) == 0:
                return None
            node = TreeNode(post[-1])
            ndex = inn.index(int(node.val))
            node.left = do_build_tree(inn[:index], post[:index])
            node.right = do_build_tree(inn[index+1:], post[index:-1])
            return node
        
        return do_build_tree(inorder, postorder)

if __name__ == "__main__":
    print(Solution().buildTree([9,3,15,20,7], [9,15,7,20,3]))


# @lc code=end

