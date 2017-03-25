class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        x, y = m - 1, n - 1
        if x == 0 or y == 0:
            return 1

        divide = range(2, min(x, y) + 1)
        result = 1

        for i in xrange(max(x, y) + 1, x + y + 1):
            current = i
            for j in range(len(divide)):
                if current % divide[j] == 0:
                    current = current / divide.pop(j)
                    break
            result = result * current

        for i in divide:
            result /= i

        return result



if __name__ == '__main__':
    assert Solution().uniquePaths(2, 1) == 1
    assert Solution().uniquePaths(3, 7) == 28
    assert Solution().uniquePaths(100, 100) == 22750883079422934966181954039568885395604168260154104734000
