class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        data = []
        i = 0
        while len(s) > 0:
            if not i % 2:
                data.append([""] * numRows)
                for j in range(numRows):
                    data[i][j] = s[0]
                    s = s[1:]
                    if len(s) == 0:
                        break
            else:
                data.append([""] * numRows)
                for j in range(1, numRows-1):
                    data[i][numRows - j - 1] = s[0]
                    s = s[1:]
                    if len(s) == 0:
                        break
            i = i + 1
        result = ""
        for m in range(numRows):
            for n in range(len(data)):
                result = result + data[n][m]
        return result
