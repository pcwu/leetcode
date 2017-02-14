class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if numRows == 0:
            return []

        pascals = [[1]]

        for i in range(1, numRows):
            pascals.append([pascals[i - 1][0]])
            for j in range(len(pascals[i - 1]) - 1):
                pascals[i].append(pascals[i - 1][j] + pascals[i - 1][j + 1])
            pascals[i].append(pascals[i - 1][-1])
        return pascals
