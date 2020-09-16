#
# @lc app=leetcode.cn id=542 lang=python
#
# [542] 01 矩阵
#

# @lc code=start
import collections

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(matrix)
        n = len(matrix[0])
        stack = collections.deque()
        dist = [[0]*n for _ in range(m)]
        print(dist)
        visited = {}
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    stack.append((i,j))
                    visited.setdefault((i,j), 1)
 
        while len(stack) > 0:
            i, j = stack.popleft()
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in visited:
                    dist[ni][nj] = dist[i][j] + 1
                    stack.append((ni, nj))
                    visited.setdefault((ni,nj), 1)
        return dist
        

if __name__ == "__main__":
    print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
        
# 0 1 0
# 0 1 0
# 0 1 0
# 0 1 0
# 0 1 0
# @lc code=end

