#
# @lc app=leetcode.cn id=200 lang=python
#
# [200] 岛屿数量
# @lc code=start
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        sum = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    sum += 1
        print(grid)
        return sum
        
    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j) 
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)
                
if __name__ == "__main__":
    print(Solution().numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))

# @lc code=end

