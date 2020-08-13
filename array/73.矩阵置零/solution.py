class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        zero_indexs = []
        for i in range(n):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    for index in range(len(matrix[i])):
                        zero_indexs.append([i, index])
                    for index in range(n):
                        if (i - index) >= 0:
                            zero_indexs.append([i - index, j])
                        if (i + index) < n:
                            zero_indexs.append([i + index, j])
        for indexs in zero_indexs:
            matrix[indexs[0]][indexs[1]] = 0
        print(matrix)
    
if __name__ == '__main__':
    Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])

                    




        
    