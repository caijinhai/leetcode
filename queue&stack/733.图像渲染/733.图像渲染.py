#
# @lc app=leetcode.cn id=733 lang=python
#
# [733] 图像渲染
#

# @lc code=start
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        oldColor = image[sr][sc]
        print(oldColor)
        stack = []
        stack.append((sr, sc))
        m = len(image)
        n = len(image[0])
        exists = {}
        while len(stack) > 0:
            sr, sc = stack.pop()
            image[sr][sc] = newColor
            exists.setdefault((sr, sc), 1)

            if sr - 1 >= 0:
                if image[sr-1][sc] == oldColor and (sr-1,sc) not in exists:
                    stack.append((sr-1, sc))
            if sr + 1 < m:
                if image[sr+1][sc] == oldColor and (sr+1,sc) not in exists:
                    stack.append((sr+1, sc))
            if sc - 1 >= 0:
                if image[sr][sc-1] == oldColor and (sr,sc-1) not in exists:
                    stack.append((sr, sc-1))
            if sc + 1 < n:
                if image[sr][sc+1] == oldColor and (sr,sc+1) not in exists:
                    stack.append((sr, sc+1))
        return image


if __name__ == "__main__":
    print(Solution().floodFill([[0,0,0],[0,1,1]], 1, 1, 1))
        
# @lc code=end