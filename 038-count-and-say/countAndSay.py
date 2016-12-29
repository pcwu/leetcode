class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        return self.say(n, "1")

    def say(self, n, value):
        if n == 1:
            return value
        elif n > 1:
            ctr = 1
            result = ""
            while len(value) >= 2:
                if value[1] == value[0]:
                    ctr += 1
                else:
                    result = result + str(ctr) + str(value[0])
                    ctr = 1
                value = value[1:]
            result = result + str(ctr) + str(value[0])
            return self.say(n - 1, result)
