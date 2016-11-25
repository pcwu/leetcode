class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ""
        while num > 0:
            if num >= 1000:
                num = num - 1000
                roman = roman + "M"
            elif num >= 900:
                num = num - 900
                roman = roman + "CM"
            elif num >= 500:
                num = num - 500
                roman = roman + "D"
            elif num >= 400:
                num = num - 400
                roman = roman + "CD"
            elif num >= 100:
                num = num - 100
                roman = roman + "C"
            elif num >= 90:
                num = num - 90
                roman = roman + "XC"
            elif num >= 50:
                num = num - 50
                roman = roman + "L"
            elif num >= 40:
                num = num - 40
                roman = roman + "XL"
            elif num >= 10:
                num = num - 10
                roman = roman + "X"
            elif num >= 9:
                num = num - 9
                roman = roman + "IX"
            elif num >= 5:
                num = num - 5
                roman = roman + "V"
            elif num >= 4:
                num = num - 4
                roman = roman + "IV"
            elif num >= 1:
                num = num - 1
                roman = roman + "I"
        return roman
