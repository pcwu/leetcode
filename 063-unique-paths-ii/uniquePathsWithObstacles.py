class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1:
            return 0

        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        array = [[0 for x in range(n)] for x in range(m)]
        array[0][0] = 1

        for i in range(1, m):
            array[i][0] = array[i - 1][0] if obstacleGrid[i][0] == 0 else 0

        for i in range(1, n):
            array[0][i] = array[0][i - 1] if obstacleGrid[0][i] == 0 else 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    array[i][j] = array[i - 1][j] + array[i][j - 1]
                else:
                    array[i][j] = 0

        return array[m - 1][n - 1]

if __name__ == '__main__':
    assert Solution().uniquePathsWithObstacles([[0]]) == 1
    assert Solution().uniquePathsWithObstacles([[0], [0]]) == 1
    assert Solution().uniquePathsWithObstacles([[0], [1]]) == 0
    assert Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]) == 2
