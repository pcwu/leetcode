class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix.reverse()
        for i in xrange(n):
            for j in xrange(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



if __name__ == '__main__':
    matrix = [[1, 2], [3, 4]]
    Solution().rotate(matrix)
    print matrix  # should be [[3,1],[4,2]]

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Solution().rotate(matrix)
    print matrix  # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
