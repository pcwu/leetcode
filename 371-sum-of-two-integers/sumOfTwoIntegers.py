class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a & b:
            if a < 0 and b < 0:
                return ~self.getSum((~a & ~b) << 1, ~a ^ ~b)
            else:
                return self.getSum((~a & ~b) << 1, ~a ^ ~b)
        else:
            return a ^ b
