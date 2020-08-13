import copy

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rotated = []
        lenx = len(matrix)
        leny = len(matrix[0])
        for x in range(lenx):
            for y in range(leny):
                rotated.append(matrix[x][y])

        for x in range(lenx):
            for y in range(leny):
                matrix[x][lenx - y - 1] = rotated[x + y * len(matrix[x])]
        return matrix
    
class Solution2(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        new_matrix = [[0] * n for _ in range(n)]
        print(new_matrix)
        for i in range(n):
            for j in range(n):
                new_matrix[j][n - i - 1] = matrix[i][j]

        matrix[:] = new_matrix
        return matrix


if __name__ == "__main__":
    print(Solution2().rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))
